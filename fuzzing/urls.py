from django.conf.urls import patterns, include, url
from django.contrib import admin

from website.views import PageView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    
    url(r'^cms/', include('fuzzing.cms.urls')),

    url(r'^$', PageView.as_view(), name='home'),
    url(r'^(?P<slug>[-\w]+)/', PageView.as_view(), name='page'),
)
