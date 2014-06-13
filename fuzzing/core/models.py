from django.conf import settings
from django.db import models
from django.utils.text import slugify

from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Submit, HTML

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


class BaseManager(models.Manager):
    def published(self):
        return self.filter(published=True)


class BaseModel(models.Model):
    published = models.BooleanField(default=True,
        help_text='Only published pages/secions will be shown in live.')
    weight = models.IntegerField(default=0,
        help_text='The higher the weight, the lower - or the righter - in the page will appear.')

    objects = BaseManager()

    class Meta:
        abstract = True
        ordering = ['weight',]

    @classmethod
    def get_basic_layout(cls):
        return Layout(
            WellFieldset('Basic details',
                'published',
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
    title = models.CharField(
        help_text='Title of the page',
        max_length=36)
    slug = models.CharField(
        blank=True,
        help_text='How the page url will appear in the browser.',
        max_length=64)
    in_navigation = models.BooleanField(
        default=True,
        help_text='Should this page be in the main navigation?')
    is_home_page = models.BooleanField(
        default=False,
        help_text='Is this the main page of the site?')
    is_long_page = models.BooleanField(
        default=False,
        help_text="""
        Is this page long? If you activate this option, you will see
        a go-up arrow at the bottom of the page
        """)
    show_social_icons = models.BooleanField(
        default=False,
        help_text='If you check this option, the page will show social icons.')
    show_share = models.BooleanField(
        default=False,
        help_text='If you check this option, the page will show a share link.')
    parent_page = models.ForeignKey(
        'Page',
        blank=True,
        null=True)
    side_offset = models.CharField(
        max_length=64,
        choices=OFFSET_CHOICES,
        default='0',
        help_text='Pick the percentage of white space you want on each side of the page.')
    left_text = models.TextField(
        blank=True,
        help_text='If you type some text here, it will appear as a fixed column on the left of the page.'
    )
    right_text = models.TextField(
        blank=True,
        help_text='If you type some text here, it will appear as a fixed column on the right of the page.'
    )

    def __unicode__(self):
        return self.title

    def get_unique_slug(self, slug):
        new_slug = slug
        counter = 1
        while Page.objects.filter(slug=new_slug).exists():
            new_slug = "%s-%s" % (slug, counter)
            counter += 1
        return new_slug

    def get_layout_size(self):
        if self.left_text and self.right_text:
            return 'one-half'
        if (self.left_text and not self.right_text) or (self.right_text and not self.left_text):
            return 'two-thirds'
        return 'one-whole'

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
            ),
            WellFieldset('Side texts',
                'left_text',
                HTML('<p>If you write text here, the page will have a left column with this content.</p>'),
                'right_text',
                HTML('<p>If you write text here, the page will have a right column with this content.</p>'),
            ),
            WellFieldset('Page layout',
                'in_navigation',
                'is_home_page',
                'side_offset',
                'is_long_page',
                'show_social_icons',
                'show_share',
            ),
            WellFieldset('Page parent',
                'parent_page',
            ),
            cls.get_button_layout()
        )

    def get_sections(self, published=True):
        page_sections = []
        for kls in SECTIONS:
            section_list = kls.objects.filter(page=self)
            if published:
                section_list = section_list.filter(published=True)
            page_sections = page_sections + [section for section in section_list]
        page_sections.sort(key=lambda x: x.weight, reverse=False)
        return page_sections

    def get_sections_cms(self):
        return self.get_sections(published=False)

    @property
    def get_relative_url(self):
        if self.is_home_page:
            return '/'
        return '/%s/' % self.slug


class Section(BaseModel):
    """"""
    page = models.ForeignKey('Page', default=None, null=True)

    class Meta:
        abstract = True

    @classmethod
    def template_name(cls):
        return 'website/sections/%s.html' % cls.__name__

    def get_class(self):
        return self.__class__.__name__


class LayoutMixin(models.Model):
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


class TextSectionMixin(models.Model):
    """"""
    title = models.CharField(blank=True, max_length=64, help_text='Title')
    text = models.TextField(blank=True, help_text='Text')

    class Meta:
        abstract = True


class ImageSectionMixin(models.Model):
    """"""
    image = models.ImageField(upload_to=settings.UPLOADS_ROOT, help_text='Image to display')

    class Meta:
        abstract = True

    def get_image_url(self):
        return '%s%s' % (settings.STATIC_URL, self.image.url)


class ImageSection(ImageSectionMixin, LayoutMixin, Section):
    """"""
    title = models.CharField(blank=True, max_length=64, help_text='Image title')

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
            ),
            WellFieldset('Section layout',
                'layout',
                'alignment',
            ),
            WellFieldset('Page containing this section',
                'page',
            ),
            cls.get_button_layout()
        )


class ImageLinkSection(ImageSectionMixin, LayoutMixin, Section):
    """"""
    title = models.CharField(blank=True, max_length=64, help_text='Link title')
    subtitle = models.CharField(blank=True, max_length=256, help_text='Link title')
    link = models.CharField(blank=True, max_length=64, help_text='To which page should this section link to?')

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
            ),
            WellFieldset('Section layout',
                'layout',
                'alignment',
            ),
            WellFieldset('Parent page',
                'page',
            ),
            cls.get_button_layout()
        )


class TextSection(TextSectionMixin, LayoutMixin, Section):
    """"""

    def preview(self):
        return '<div class="section">\
                    <span class="section__title">%s</span>\
                </div>' % self.title

    @classmethod
    def get_form_layout(cls):
        return Layout(
            cls.get_basic_layout(),
            WellFieldset('Section details',
                'title',
                'text',
            ),
            WellFieldset('Section layout',
                'layout',
                'alignment',
            ),
            WellFieldset('Parent page',
                'page',
            ),
            cls.get_button_layout()
        )


class BackgroundImageTextSection(ImageSectionMixin, TextSectionMixin, Section):
    """"""
    BACKGROUND_POSITION_CHOICES = (
        ('top', 'Top'),
        ('center', 'Center'),
        ('bottom', 'Bottom'),
    )
    TEXT_COLOR_CHOICES = (
        ('#ffffff', 'White'),
        ('#000000', 'Black'),
    )
    TEXT_SIDE_CHOICES = (
        ('left', 'Left'),
        ('right', 'Right'),
    )

    background_position = models.CharField(
        choices=BACKGROUND_POSITION_CHOICES,
        default='center',
        max_length=64,
        help_text='What alignment do you want for the background image?'
    )
    text_color = models.CharField(
        choices=TEXT_COLOR_CHOICES,
        default='#000000',
        max_length=64,
        help_text='Text color for this section?'
    )
    text_side = models.CharField(
        choices=TEXT_SIDE_CHOICES,
        default='left',
        max_length=64,
        help_text='Where do you want the text to appear?'
    )

    def preview(self):
        return '<div class="section">\
                    <p><strong>background image:</strong> %s</p>\
                    <span class="section__title">%s</span>\
                </div>' % (self.image, self.title)

    @classmethod
    def get_form_layout(cls):
        return Layout(
            cls.get_basic_layout(),
            WellFieldset('Section details',
                'title',
                'text',
                'image',
                'text_color',
                'text_side',
                'background_position',
            ),
            WellFieldset('Section\'s page',
                'page',
            ),
            cls.get_button_layout()
        )


SECTIONS = (
    BackgroundImageTextSection,
    ImageLinkSection,
    ImageSection,
    TextSection,
)
