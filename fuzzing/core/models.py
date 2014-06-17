from django.conf import settings
from django.db import models
from django.utils.text import slugify

from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Submit, HTML

from fuzzing.cms.fields import WellFieldset

LAYOUT_CHOICES = (
    (u'one-whole', u'One Whole'),
    (u'one-half', u'One Half'),
    (u'one-third', u'One Third'),
    (u'one-quarter', u'One Quarter'),
    (u'two-thirds', u'Two Thirds'),
)

LAYOUT_CMS = {
    u'one-whole': u'col-lg-12',
    u'one-half': u'col-lg-6',
    u'one-third': u'col-lg-4',
    u'one-quarter': u'col-lg-3',
    u'two-thirds': u'col-lg-8',
}

OFFSET_CMS = {
    u'no-offset': u'no-offset',
    u'offset--one-quarter': u'col-lg-offset-3',
    u'offset--one-third': u'col-lg-offset-4',
    u'offset--one-half': u'col-lg-offset-2',
    u'offset--two-thirds': u'col-lg-offset-8',
}

ALIGNMENT_CHOICES = (
    (u'top', u'Top Aligned'),
    (u'middle', u'Middle Aligned'),
    (u'bottom', u'Bottom Aligned'),
)

SECTION_OFFSET_CHOICES = (
    (u'no-offset', u'No offset'),
    (u'offset--one-quarter', u'One Quarter'),
    (u'offset--one-third', u'One Third'),
    (u'offset--one-half', u'One Half'),
    (u'offset--two-thirds', u'Two Thirds'),
)

OFFSET_CHOICES = (
    (u'0', u'No offset'),
    (u'5%', u'5%'),
    (u'10%', u'10%'),
    (u'15%', u'15%'),
    (u'20%', u'20%'),
    (u'25%', u'25%'),
)


class SiteSettings(models.Model):
    """
    Site settings
    - control the app name, which will appear in all pages titles and in the navigation bar.
    - pick the theme for the site.
    """
    site_name = models.CharField(max_length=255, blank=True)
    site_theme = models.CharField(
        max_length=255,
        blank=True,
        choices=settings.THEME_CHOICES)

    @classmethod
    def get_form_layout(cls):
        return Layout(
            WellFieldset('Site settings',
                'site_name',
                'site_theme',
            ),
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
        'self',
        blank=True,
        null=True,
        related_name='parent',
        help_text='Does this page has a parent page?')
    redirect_page = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='redirect',
        help_text='Should this page redirect to another page?')
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

    def get_url(self):
        if self.redirect_page:
            return self.redirect_page.slug
        return self.slug

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
            WellFieldset('Page redirect',
                'redirect_page',
            ),
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
    offset = models.CharField(
        max_length=64,
        choices=SECTION_OFFSET_CHOICES,
        default='no-offset',
        help_text='Some offset on the side?')
    alignment = models.CharField(
        max_length=64,
        choices=ALIGNMENT_CHOICES,
        default='top',
        help_text="""Vertical alignment of this section, useful when there
        is text and an image next to it.""")

    class Meta:
        abstract = True

    def layout_cms(self):
        return LAYOUT_CMS[self.layout]

    def offset_cms(self):
        if self.offset:
            return OFFSET_CMS[self.offset]
        return ''


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
        return """<div class="section">
                    <img src="%s">
                    <span class="section__title">%s</span>
                </div>""" % (self.get_image_url(), self.title)

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
                'offset',
                'alignment',
            ),
            WellFieldset('Page containing this section',
                'page',
            ),
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

    def preview(self):
        return """<div class="section">
                    <img src="%s">
                    <span class="section__title">%s</span>
                    <span class="section__link">Link to: %s</span>
                </div>""" % (self.get_image_url(), self.title, self.link)


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
                'offset',
                'alignment',
            ),
            WellFieldset('Parent page',
                'page',
            ),
        )


class VideoSection(LayoutMixin, Section):
    """"""
    title = models.CharField(blank=True, max_length=64, help_text='Link title')
    youtube_id = models.CharField(
        blank=True,
        max_length=256,
        help_text='Youtube video id')
    vimeo_id = models.CharField(
        blank=True,
        max_length=256,
        help_text='Vimeo video id')
    height = models.CharField(
        blank=True,
        default='360px',
        max_length=256,
        help_text='Percentage or pixels of video height.'
    )
    width = models.CharField(
        blank=True,
        default='100%',
        max_length=256,
        help_text='Percentage or pixels of video width.'
    )

    def get_height(self):
        return self.height.replace('px', '')

    def get_width(self):
        return self.width.replace('px', '')

    def preview(self):
        return '<div class="section">\
                    <span class="section__title">%s</span>\
                    <p class="section__video">%s</p>\
                    <p class="section__size">%sx%s</p>\
                </div>' % (self.title, self.youtube_id, self.width, self.height)

    @classmethod
    def get_form_layout(cls):
        return Layout(
            cls.get_basic_layout(),
            WellFieldset(
                'Section details',
                'title',
                'youtube_id',
                'vimeo_id',
                'width',
                'height',
            ),
            WellFieldset(
                'Section layout',
                'layout',
                'offset',
                'alignment',
            ),
            WellFieldset(
                'Page containing this section',
                'page',
            ),
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
                'offset',
                'alignment',
            ),
            WellFieldset('Parent page',
                'page',
            ),
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
        )


class SeparatorSection(Section):
    @classmethod
    def get_form_layout(cls):
        return Layout(
            cls.get_basic_layout(),
            WellFieldset('Section\'s page',
                'page',
            ),
        )


SECTIONS = (
    BackgroundImageTextSection,
    ImageLinkSection,
    ImageSection,
    TextSection,
    VideoSection,
    SeparatorSection,
)
