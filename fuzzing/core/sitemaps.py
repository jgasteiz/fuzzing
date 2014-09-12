from django.contrib import sitemaps

from .models import Page


class PagesSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Page.objects.all()

    def location(self, page):
        return page.get_relative_url
