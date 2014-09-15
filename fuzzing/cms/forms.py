from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse

from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Submit, HTML
from crispy_forms.helper import FormHelper
from tinymce.widgets import TinyMCE

from fuzzing.core import models

TRANSLATABLE_PROPERTIES = (
    'title',
    'subtitle',
    'text',
    'right_text',
    'left_text',
)

TEXT_PROPERTIES = (
    'text',
    'right_text',
    'left_text',
)


class FormHelperMixin(object):
    def __init__(self, *args, **kwargs):
        super(FormHelperMixin, self).__init__(*args, **kwargs)
        helper = FormHelper()
        helper.form_class = 'form'
        self.helper = helper
        self.model = self.instance.__class__
        self.helper.layout = Layout(
            self.model.get_form_layout(),
            self.get_button_layout()
        )
        lang_diff = [lang for lang, lang_text in settings.LANGUAGES if lang not in settings.DISPLAY_LANGUAGES]
        for prop in TRANSLATABLE_PROPERTIES:
            if hasattr(self.instance, prop):
                for language in lang_diff:
                    property_name = '%s_%s' % (prop, language)
                    self.fields.pop(property_name, None)

            if prop in TEXT_PROPERTIES and hasattr(self.instance, prop):
                for language in settings.DISPLAY_LANGUAGES:
                    property_name = '%s_%s' % (prop, language)
                    self.fields[property_name].required = False
                    self.fields[property_name].widget = TinyMCE(attrs={'cols': 120, 'rows': 20})

    def get_button_layout(self):
        return Layout(
            FormActions(
                Submit('submit', 'Submit'),
                HTML('<a class="btn btn-default" href="%s">Cancel</a>' % self.get_cancel_url()),
            )
        )

    def get_cancel_url(self):
        pass


class SiteSettingsForm(FormHelperMixin, forms.ModelForm):
    class Meta:
        model = models.SiteSettings

    def get_cancel_url(self):
        return reverse('settings', kwargs={'pk': self.instance.pk})


class PageForm(FormHelperMixin, forms.ModelForm):

    class Meta:
        model = models.Page

    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        page_qs = models.Page.objects.exclude(pk=self.instance.pk)
        self.fields['parent_page'] = forms.ModelChoiceField(queryset=page_qs, required=False)

    def get_cancel_url(self):
        if self.instance.pk:
            return reverse('page_detail', kwargs={'pk': self.instance.pk})
        return reverse('page_list')


class SectionFormMixin(FormHelperMixin):
    def get_cancel_url(self):
        if self.instance.page:
            return reverse('page_detail', kwargs={'pk': self.instance.page.pk})
        return reverse('page_list')


class BackgroundImageTextSectionForm(SectionFormMixin, forms.ModelForm):
    text_es = forms.CharField(
        required=False, widget=TinyMCE(attrs={'cols': 120, 'rows': 20}))
    text_en = forms.CharField(
        required=False, widget=TinyMCE(attrs={'cols': 120, 'rows': 20}))
    text_ca = forms.CharField(
        required=False, widget=TinyMCE(attrs={'cols': 120, 'rows': 20}))

    class Meta:
        model = models.BackgroundImageTextSection


class ImageSectionForm(SectionFormMixin, forms.ModelForm):
    class Meta:
        model = models.ImageSection


class ImageLinkSectionForm(SectionFormMixin, forms.ModelForm):
    class Meta:
        model = models.ImageLinkSection

    def __init__(self, *args, **kwargs):
        super(ImageLinkSectionForm, self).__init__(*args, **kwargs)
        pages = models.Page.objects.published().exclude(is_home_page=True)
        choices = [(page.slug, page.title) for page in pages]
        self.fields['link'] = forms.ChoiceField(choices=choices)


class TextSectionForm(SectionFormMixin, forms.ModelForm):
    text_es = forms.CharField(
        required=False, widget=TinyMCE(attrs={'cols': 120, 'rows': 20}))
    text_en = forms.CharField(
        required=False, widget=TinyMCE(attrs={'cols': 120, 'rows': 20}))
    text_ca = forms.CharField(
        required=False, widget=TinyMCE(attrs={'cols': 120, 'rows': 20}))

    class Meta:
        model = models.TextSection


class VideoSectionForm(SectionFormMixin, forms.ModelForm):
    class Meta:
        model = models.VideoSection


class SeparatorSectionForm(SectionFormMixin, forms.ModelForm):
    class Meta:
        model = models.SeparatorSection
