from django import forms

from crispy_forms.helper import FormHelper

from fuzzing.core import models


class FormHelperMixin(object):
    def get_form_helper(self):
        helper = FormHelper()
        helper.form_class = 'form'
        return helper

    def __init__(self, *args, **kwargs):
        super(FormHelperMixin, self).__init__(*args, **kwargs)
        self.helper = self.get_form_helper()
        self.model = self.instance.__class__
        self.helper.layout = self.model.get_form_layout()


class PageForm(FormHelperMixin, forms.ModelForm):
    class Meta:
        model = models.Page

    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        page_qs = models.Page.objects.exclude(pk=self.instance.pk)
        self.fields['parent_page'] = forms.ModelChoiceField(queryset=page_qs, required=False)


class ImageSectionForm(FormHelperMixin, forms.ModelForm):
    class Meta:
        model = models.ImageSection


class ImageLinkSectionForm(FormHelperMixin, forms.ModelForm):
    class Meta:
        model = models.ImageLinkSection

    def __init__(self, *args, **kwargs):
        super(ImageLinkSectionForm, self).__init__(*args, **kwargs)
        pages = models.Page.objects.exclude(is_home_page=True)
        choices = [(page.slug, page.title) for page in pages]
        self.fields['link'] = forms.ChoiceField(choices=choices)


class TextSectionForm(FormHelperMixin, forms.ModelForm):
    class Meta:
        model = models.TextSection
