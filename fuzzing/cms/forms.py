from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Submit, HTML
from django import forms

from crispy_forms.helper import FormHelper
from django.core.urlresolvers import reverse
from tinymce.widgets import TinyMCE

from fuzzing.core import models


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
    left_text = forms.CharField(required=False, widget=TinyMCE(attrs={'cols': 120, 'rows': 20}))
    right_text = forms.CharField(required=False, widget=TinyMCE(attrs={'cols': 120, 'rows': 20}))

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
    text = forms.CharField(required=False, widget=TinyMCE(attrs={'cols': 120, 'rows': 20}))

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
    text = forms.CharField(required=False, widget=TinyMCE(attrs={'cols': 120, 'rows': 20}))

    class Meta:
        model = models.TextSection


class VideoSectionForm(SectionFormMixin, forms.ModelForm):
    class Meta:
        model = models.VideoSection


class SeparatorSectionForm(SectionFormMixin, forms.ModelForm):
    class Meta:
        model = models.SeparatorSection
