from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView
from django.conf import settings

from fuzzing.core import models


class PageView(DetailView):
    """
    Main view for rendering pages.
    """
    template_name = 'website/page.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(PageView, self).get_context_data(*args, **kwargs)

        page_list = models.Page.objects.filter(in_navigation=True)

        # Create a list of nav_items with pages slugs and titles.
        ctx['nav_item_list'] = [{'slug': page.slug, 'title': page.title} for page in page_list]
        ctx['site_settings'] = models.SiteSettings.objects.get_or_create()[0]

        if self.kwargs and self.kwargs['slug']:
            ctx['current_page'] = self.kwargs['slug']
        return ctx

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
