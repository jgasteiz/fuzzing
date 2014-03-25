from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView

from fuzzing.core.models import Page, SiteSettings


class PageView(DetailView):
    """
    Main view for rendering pages.
    """
    template_name = 'website/theme/page.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(PageView, self).get_context_data(*args, **kwargs)

        page_list = Page.objects.filter(in_navigation=True)
        site_settings = SiteSettings.objects.get_or_create()[0]

        # Create a list of nav_items with pages slugs and titles.
        ctx['nav_item_list'] = (
            [{'slug': page.slug, 'title': page.title} for page in page_list]
        )
        ctx['site_settings'] = site_settings

        # Replace the `theme` directory with the current theme.
        self.template_name = self.template_name.replace('theme', site_settings.site_theme)

        if self.kwargs and self.kwargs['slug']:
            ctx['current_page'] = self.kwargs['slug']

        # Check if current page has children and pick them for the sub nav.
        page_children = Page.objects.filter(parent_page=self.object)
        if page_children:
            ctx['sub_nav_item_list'] = (
                [{'slug': page.slug, 'title': page.title} for page in page_children]
            )

        # Check if current page has parent and pick its siblings for the sub nav.
        if self.object.parent_page:
            page_siblings = Page.objects.filter(parent_page=self.object.parent_page)
            ctx['sub_nav_item_list'] = (
                [{'slug': page.slug, 'title': page.title} for page in page_siblings]
            )

        if 'current_page' in ctx or 'nav-open' in self.request.GET:
            ctx['nav_open'] = True

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
            return get_object_or_404(Page, slug=page_slug)
        else:
            return get_object_or_404(Page, is_home_page=True)
