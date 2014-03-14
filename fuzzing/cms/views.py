from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.shortcuts import redirect, get_object_or_404

from fuzzing.core import models
from fuzzing.cms import forms

SECTIONS_DICT = {
    'ImageSection': {
        'model': models.ImageSection,
        'form_class': forms.ImageSectionForm
    },
    'ImageLinkSection': {
        'model': models.ImageLinkSection,
        'form_class': forms.ImageLinkSectionForm
    },
    'TextSection': {
        'model': models.TextSection,
        'form_class': forms.TextSectionForm
    },
}


class CMSMixin(object):
    def get_context_data(self, *args, **kwargs):
        ctx = super(CMSMixin, self).get_context_data(*args, **kwargs)
        ctx['url'] = self.url
        ctx['section_list'] = sorted(list(SECTIONS_DICT))
        ctx['app_title'] = settings.APP_TITLE
        return ctx


# Pages
class PagesView(CMSMixin, generic.ListView):
    context_object_name = "page_list"
    model = models.Page
    template_name = 'cms/pages.html'
    url = 'page'

pages = PagesView.as_view()


class CreatePage(CMSMixin, generic.edit.CreateView):
    form_class = forms.PageForm
    model = models.Page
    template_name = 'cms/page_create.html'
    success_url = reverse_lazy('pages')
    url = 'page'

create_page = CreatePage.as_view()


class UpdatePage(CMSMixin, generic.edit.UpdateView):
    form_class = forms.PageForm
    model = models.Page
    template_name = 'cms/page_update.html'
    success_url = reverse_lazy('pages')
    url = 'page'

update_page = UpdatePage.as_view()


class DeletePage(CMSMixin, generic.edit.DeleteView):
    model = models.Page
    template_name = 'cms/page_confirm_delete.html'
    success_url = reverse_lazy('pages')
    url = 'page'

delete_page = DeletePage.as_view()


class ChangePageWeight(CMSMixin, generic.edit.View):
    success_url = reverse_lazy('pages')

    def get(self, request, *args, **kwargs):
        pk = int(self.kwargs['pk'])
        weight = int(self.kwargs['weight'])
        page = get_object_or_404(models.Page, pk=pk)
        if weight < 0:
            page.decrease_weight()
        else:
            page.increase_weight()
        return redirect(self.success_url)

change_page_weight = ChangePageWeight.as_view()


# Sections
class SectionObjectsMixin(object):
    def get_form_class(self):
        section_name = self.kwargs['section']
        self.form_class = SECTIONS_DICT[section_name]['form_class']
        return self.form_class


class CreateSection(SectionObjectsMixin, CMSMixin, generic.edit.CreateView):
    template_name = 'cms/section_create.html'
    success_url = reverse_lazy('pages')
    url = 'section'

    def get_initial(self):
        initial = super(CreateSection, self).get_initial()
        initial['page'] = int(self.kwargs['page_pk'])
        return initial

create_section = CreateSection.as_view()


class UpdateSection(SectionObjectsMixin, CMSMixin, generic.edit.UpdateView):
    template_name = 'cms/section_update.html'
    success_url = reverse_lazy('pages')
    url = 'section'

    def get_form_kwargs(self):
        self.object = self.get_object()
        kwargs = super(UpdateSection, self).get_form_kwargs()
        kwargs.update({'instance': self.object})
        return kwargs

    def get_object(self, queryset=None):
        section_name = self.kwargs['section']
        pk = int(self.kwargs['pk'])
        self.object = get_object_or_404(SECTIONS_DICT[section_name]['model'], pk=pk)
        self.model = SECTIONS_DICT[section_name]['model']
        self.queryset = SECTIONS_DICT[section_name]['model'].objects.all()
        return self.object


update_section = UpdateSection.as_view()


class DeleteSection(CMSMixin, generic.edit.DeleteView):
    template_name = 'cms/section_confirm_delete.html'
    success_url = reverse_lazy('pages')
    url = 'section'

    def get_object(self, queryset=None):
        section_name = self.kwargs['section']
        pk = int(self.kwargs['pk'])
        self.object = get_object_or_404(SECTIONS_DICT[section_name]['model'], pk=pk)
        self.model = SECTIONS_DICT[section_name]['model']
        return self.object

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)

delete_section = DeleteSection.as_view()


class ChangeSectionWeight(CMSMixin, generic.edit.View):
    success_url = reverse_lazy('pages')

    def get(self, request, *args, **kwargs):
        pk = int(self.kwargs['pk'])
        section_name = self.kwargs['section']
        weight = int(self.kwargs['weight'])
        section = get_object_or_404(SECTIONS_DICT[section_name]['model'], pk=pk)
        if weight < 0 and section.weight > 0:
            section.weight = section.weight - 1
            section.save()
        elif weight > 0:
            section.weight = section.weight + 1
            section.save()
        return redirect(self.success_url)

change_section_weight = ChangeSectionWeight.as_view()
