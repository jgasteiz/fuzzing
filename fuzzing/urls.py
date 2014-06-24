from django.conf.urls import patterns, include, url
from django.contrib import admin

from website.views import PageView, customHandler404, customHandler500

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^localeurl/', include('localeurl.urls')),
    url(r'^cms/', include('fuzzing.cms.urls')),

    url(r'^$', PageView.as_view(), name='home'),
    url(r'^(?P<slug>[-\w]+)/', PageView.as_view(), name='page'),
)

handler404 = customHandler404
handler500 = customHandler500
