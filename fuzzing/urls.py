from django.conf.urls import patterns, include, url
from django.contrib import admin

from website.sitemaps import PagesSiteMap
from website.views import PageView, custom_handler_404, custom_handler_500

admin.autodiscover()

sitemaps = {
    'static': PagesSiteMap
}

urlpatterns = patterns('',
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^localeurl/', include('localeurl.urls')),
    url(r'^cms/', include('fuzzing.cms.urls')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    url(r'^$', PageView.as_view(), name='home'),
    url(r'^(?P<slug>[-\w]+)/', PageView.as_view(), name='page'),
)

handler404 = custom_handler_404
handler500 = custom_handler_500
