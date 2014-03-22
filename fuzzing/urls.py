from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    
    url(r'^cms/', include('fuzzing.cms.urls')),

    url(r'^$', 'fuzzing.website.views.page', name='home'),
    url(r'^(?P<slug>[-\w]+)/', 'fuzzing.website.views.page', name='page'),
)
