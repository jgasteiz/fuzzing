from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.debug import sensitive_post_parameters

from fuzzing.core import models

from . import forms


SECTIONS_DICT = {
    'BackgroundImageTextSection': {
        'model': models.BackgroundImageTextSection,
        'form_class': forms.BackgroundImageTextSectionForm
    },
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
    'VideoSection': {
        'model': models.VideoSection,
        'form_class': forms.VideoSectionForm
    },
    'SeparatorSection': {
        'model': models.SeparatorSection,
        'form_class': forms.SeparatorSectionForm
    },
}


# Auth
class Login(generic.FormView):
    form_class = AuthenticationForm
    template_name = 'cms/login.html'

    def form_valid(self, form):
        redirect_to = settings.LOGIN_REDIRECT_URL
        auth_login(self.request, form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return HttpResponseRedirect(redirect_to)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    @method_decorator(sensitive_post_parameters('password'))
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(Login, self).dispatch(request, *args, **kwargs)


class Logout(generic.View):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)


class CMSMixin(object):
    """
    Ensures that user must be authenticated in order to access view.

    Taken from: https://djangosnippets.org/snippets/2442/
    """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CMSMixin, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        ctx = super(CMSMixin, self).get_context_data(*args, **kwargs)
        ctx['current_user'] = self.request.user
        ctx['section_list'] = sorted(list(SECTIONS_DICT))
        ctx['site_settings'] = models.SiteSettings.objects.get_or_create()[0]
        ctx['url'] = self.url
        return ctx


# Site settings
class SiteSettingsView(CMSMixin, generic.DetailView):
    model = models.SiteSettings
    template_name = 'cms/settings.html'
    url = 'settings'


class UpdateSiteSettings(CMSMixin, generic.edit.UpdateView):
    form_class = forms.SiteSettingsForm
    model = models.SiteSettings
    template_name = 'cms/settings_update.html'
    url = 'settings'

    def get_success_url(self):
        return reverse('settings', kwargs={'pk': self.object.pk})


# Pages
class PageList(CMSMixin, generic.ListView):
    context_object_name = "page_list"
    model = models.Page
    template_name = 'cms/page_list.html'
    url = 'page'


class PageDetail(CMSMixin, generic.DetailView):
    context_object_name = "page"
    model = models.Page
    template_name = 'cms/page_detail.html'
    url = 'page'


class CreatePage(CMSMixin, generic.edit.CreateView):
    form_class = forms.PageForm
    model = models.Page
    template_name = 'cms/page_create.html'
    url = 'page'

    def get_success_url(self):
        return reverse('page_detail', kwargs={'pk': self.object.pk})


class UpdatePage(CMSMixin, generic.edit.UpdateView):
    form_class = forms.PageForm
    model = models.Page
    template_name = 'cms/page_update.html'
    url = 'page'

    def get_success_url(self):
        return reverse('page_detail', kwargs={'pk': self.object.pk})


class DeletePage(CMSMixin, generic.edit.DeleteView):
    model = models.Page
    template_name = 'cms/page_confirm_delete.html'
    success_url = reverse_lazy('page_list')
    url = 'page'


class SetPageWeight(CMSMixin, generic.edit.View):
    success_url = reverse_lazy('page_list')

    def get(self, request, *args, **kwargs):
        pk = int(self.kwargs['pk'])
        weight = int(self.kwargs['weight'])
        page = get_object_or_404(models.Page, pk=pk)
        if weight < 0:
            page.decrease_weight()
        else:
            page.increase_weight()
        return redirect(self.success_url)


# Sections
class SectionObjectsMixin(object):
    def get_form_class(self):
        section_name = self.kwargs['section']
        self.form_class = SECTIONS_DICT[section_name]['form_class']
        return self.form_class


class CreateSection(SectionObjectsMixin, CMSMixin, generic.edit.CreateView):
    template_name = 'cms/section_create.html'
    url = 'section'

    def get_initial(self):
        initial = super(CreateSection, self).get_initial()
        initial['page'] = int(self.kwargs['page_pk'])
        return initial

    def get_success_url(self):
        return reverse('page_detail', kwargs={'pk': self.kwargs['page_pk']})


class UpdateSection(SectionObjectsMixin, CMSMixin, generic.edit.UpdateView):
    template_name = 'cms/section_update.html'
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

    def get_success_url(self):
        return reverse('page_detail', kwargs={'pk': self.object.page.pk})



class DeleteSection(CMSMixin, generic.edit.DeleteView):
    template_name = 'cms/section_confirm_delete.html'
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
        return self.get_success_url()

    def get_success_url(self):
        return reverse('page_detail', kwargs={'pk': self.object.page.pk})


class SetSectionWeight(CMSMixin, generic.edit.View):
    def get(self, request, *args, **kwargs):
        pk = int(self.kwargs['pk'])
        section_name = self.kwargs['section']
        weight = int(self.kwargs['weight'])
        section = get_object_or_404(SECTIONS_DICT[section_name]['model'], pk=pk)

        if weight < 0:
            new_weight = section.weight - 1 if section.weight > 0 else 0
        elif weight > 0:
            new_weight = section.weight + 1
        else:
            new_weight = section.weight

        ordered_sections = list(section.page.get_sections())
        section_index = ordered_sections.index(section)
        section = ordered_sections.pop(section_index)
        ordered_sections.insert(new_weight, section)

        for i in range(0, len(ordered_sections)):
            ordered_sections[i].weight = i
            ordered_sections[i].save()

        return redirect(reverse('page_detail', kwargs={'pk': section.page.pk}))
