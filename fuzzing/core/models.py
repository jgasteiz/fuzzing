from django.conf import settings
from django.db import models
from django.utils.text import slugify

from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Div, Field, Submit, HTML

from fuzzing.cms.fields import WellFieldset

LAYOUT_CHOICES = (
    ('one-whole', 'One Whole'),
    ('one-half', 'One Half'),
    ('one-third', 'One Third'),
    ('one-quarter', 'One Quarter'),
    ('two-thirds', 'Two Thirds'),
)

ALIGNMENT_CHOICES = (
    ('top', 'Top Aligned'),
    ('middle', 'Middle Aligned'),
    ('bottom', 'Bottom Aligned'),
)

OFFSET_CHOICES = (
    ('0', 'No offset'),
    ('5%', '5%'),
    ('10%', '10%'),
    ('15%', '15%'),
    ('20%', '20%'),
    ('25%', '25%'),
)


class SiteSettings(models.Model):
    """
    Site settings
    - control the app name, which will appear in all pages titles and in the navigation bar.
    - pick the theme for the site.
    """
    site_name = models.CharField(max_length=255, blank=True)
    site_theme = models.CharField(max_length=255, blank=True, choices=settings.THEME_CHOICES)

    @classmethod
    def get_form_layout(cls):
        return Layout(
            WellFieldset('Site Settings',
                'site_name',
                'site_theme',
            ),
            FormActions(
                Submit('submit', 'Submit'),
                HTML('<a class="btn btn-default" href="{% url \'pages\' %}">Cancel</a>'),
            )
        )


class BaseModel(models.Model):
    weight = models.IntegerField(default=0,
        help_text='The higher the weight, the lower - or the righter - in the page will appear.')

    class Meta:
        abstract = True
        ordering = ['weight',]

    @classmethod
    def get_basic_layout(cls):
        return Layout(
            WellFieldset('Basic details',
                'weight',
            )
        )

    @classmethod
    def get_button_layout(cls):
        return Layout(
            FormActions(
                Submit('submit', 'Submit'),
                HTML('<a class="btn btn-default" href="{% url \'pages\' %}">Cancel</a>'),
            )
        )

    def increase_weight(self):
        self.weight += 1
        self.save()

    def decrease_weight(self):
        if self.weight > 0:
            self.weight -= 1
            self.save()


class Page(BaseModel):
    """"""
    title = models.CharField(max_length=36, help_text='Title of the page')
    slug = models.CharField(max_length=64, blank=True, help_text='How the page url will appear in the browser.')
    in_navigation = models.BooleanField(default=True, help_text='Should this page be in the main navigation?')
    is_home_page = models.BooleanField(default=False, help_text='Is this the main page of the site?')
    parent_page = models.ForeignKey('Page', blank=True, null=True)
    side_offset = models.CharField(
        max_length=64,
        choices=OFFSET_CHOICES,
        default='0',
        help_text='Side offset percentage for the page.')

    def __unicode__(self):
        return self.title

    def get_unique_slug(self, slug):
        new_slug = slug
        counter = 1
        while Page.objects.filter(slug=new_slug).exists():
            new_slug = "%s-%s" % (slug, counter)
            counter += 1
        return new_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            possible_slug = slugify(self.title)
            self.slug = self.get_unique_slug(possible_slug)

        # There can only be one home page
        if self.is_home_page is True:
            rest_of_pages = Page.objects.exclude(pk=self.pk)
            rest_of_pages.update(is_home_page=False)

        super(Page, self).save(*args, **kwargs)

    @classmethod
    def get_form_layout(cls):
        return Layout(
            cls.get_basic_layout(),
            WellFieldset('Page details',
                'title',
                'slug',
                'in_navigation',
                'is_home_page',
                'parent_page',
                'side_offset',
            ),
            cls.get_button_layout()
        )

    def get_sections(self):
        page_sections = []
        for kls in SECTIONS:
            page_sections = page_sections + [section for section in kls.objects.filter(page=self)]
        page_sections.sort(key=lambda x: x.weight, reverse=False)
        return page_sections

    @property
    def get_relative_url(self):
        if self.is_home_page:
            return '/'
        return '/%s/' % self.slug


class Section(BaseModel):
    """"""
    layout = models.CharField(
        max_length=64,
        choices=LAYOUT_CHOICES,
        default='one-whole',
        help_text='Size of this section in the layout.')

    alignment = models.CharField(
        max_length=64,
        choices=ALIGNMENT_CHOICES,
        default='top',
        help_text='Alignment of this section.')

    class Meta:
        abstract = True

    @classmethod
    def template_name(cls):
        return 'website/sections/%s.html' % cls.__name__

    def get_class(self):
        return self.__class__.__name__


class ImageSectionMixin(models.Model):
    image = models.ImageField(upload_to=settings.UPLOADS_ROOT, help_text='Image to display')

    class Meta:
        abstract = True

    def get_image_url(self):
        return '%s%s' % (settings.STATIC_URL, self.image.url)


class ImageSection(ImageSectionMixin, Section):
    """"""
    title = models.CharField(blank=True, max_length=64, help_text='Image title')
    page = models.ForeignKey('Page', default=None, null=True)

    def preview(self):
        return '<div class="section">\
                    <span class="section__title">%s</span>\
                    <p class="section__image">%s ...</p>\
                </div>' % (self.title, self.image)

    @classmethod
    def get_form_layout(cls):
        return Layout(
            cls.get_basic_layout(),
            WellFieldset('Section details',
                'title',
                'image',
                'page',
                'layout',
                'alignment',
            ),
            cls.get_button_layout()
        )


class ImageLinkSection(ImageSectionMixin, Section):
    """"""
    title = models.CharField(blank=True, max_length=64, help_text='Link title')
    subtitle = models.CharField(blank=True, max_length=256, help_text='Link title')
    link = models.CharField(blank=True, max_length=64, help_text='To which page should this section link to?')
    page = models.ForeignKey('Page', default=None, null=True)

    def preview(self):
        return '<div class="section">\
                    <span class="section__title">%s</span>\
                    <p class="section__link-to">%s ...</p>\
                </div>' % (
                    self.title,
                    self.link)

    @classmethod
    def get_form_layout(cls):
        return Layout(
            cls.get_basic_layout(),
            WellFieldset('Section details',
                'title',
                'subtitle',
                'link',
                'image',
                'page',
                'layout',
                'alignment',
            ),
            cls.get_button_layout()
        )


class TextSection(Section):
    """"""
    title = models.CharField(blank=True, max_length=64, help_text='Title')
    text = models.TextField(blank=True, help_text='Text')
    page = models.ForeignKey('Page', default=None, null=True)

    def preview(self):
        return '<div class="section">\
                    <span class="section__title">%s</span>\
                    <p class="section__text">%s ...</p>\
                </div>' % (self.title, self.text[:16])

    @classmethod
    def get_form_layout(cls):
        return Layout(
            cls.get_basic_layout(),
            WellFieldset('Section details',
                'title',
                'text',
                'page',
                'layout',
                'alignment',
            ),
            cls.get_button_layout()
        )


SECTIONS = [ImageSection, ImageLinkSection, TextSection]
