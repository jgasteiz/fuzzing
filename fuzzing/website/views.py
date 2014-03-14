from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.views.generic import detail
from django.conf import settings

from fuzzing.core import models


class NavigationItemsMixin(object):
    def get_context_data(self, *args, **kwargs):
        ctx = super(NavigationItemsMixin, self).get_context_data(*args, **kwargs)
        page_list = models.Page.objects.filter(in_navigation=True)
        ctx['nav_item_list'] = [{'slug': page.slug, 'title': page.title} for page in page_list]
        ctx['app_title'] = settings.APP_TITLE
        if len(ctx['nav_item_list']) > 0:
            ctx['first_page'] = '/%s/' % ctx['nav_item_list'][0]['slug']
        if self.kwargs and self.kwargs['slug']:
            ctx['current_page'] = self.kwargs['slug']
        return ctx


class PageView(NavigationItemsMixin, generic.DetailView):
    template_name = 'website/page.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if 'slug' in self.kwargs and self.object.is_home_page:
            return redirect(reverse('home'))

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_object(self):
        page_slug = self.kwargs.get('slug', None)
        if page_slug:
            return get_object_or_404(models.Page, slug=page_slug)
        else:
            return get_object_or_404(models.Page, is_home_page=True)

page = PageView.as_view()
