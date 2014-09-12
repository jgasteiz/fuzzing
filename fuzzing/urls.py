from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from fuzzing.core.sitemaps import PagesSitemap
from website.views import PageView

admin.autodiscover()

sitemaps = {
    'pages': PagesSitemap
}

urlpatterns = patterns('',
    url(r'^_admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^cms/', include('fuzzing.cms.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)

urlpatterns += i18n_patterns('',
    url(r'^$', PageView.as_view(), name='home'),
    url(r'^(?P<slug>[-\w]+)/', PageView.as_view(), name='page'),
)
