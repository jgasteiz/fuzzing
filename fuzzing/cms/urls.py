from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('fuzzing.cms.views',

    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),

    url(r'^$', 'pages', name='pages'),
    url(r'^pages/$', 'pages', name='pages'),
    url(r'^create_page/$', 'create_page', name='create_page'),
    url(r'^update_page/(?P<pk>[-\d]+)/$', 'update_page', name='update_page'),
    url(r'^delete_page/(?P<pk>[-\d]+)/$', 'delete_page', name='delete_page'),
    url(r'^change_page_weight/(?P<pk>[-\d]+)/(?P<weight>[-\d]+)/$', 'change_page_weight', name='change_page_weight'),

    url(r'^create_section/(?P<page_pk>[-\d]+)/(?P<section>[-\w]+)/$', 'create_section', name='create_section'),
    url(r'^update_section/(?P<pk>[-\d]+)/(?P<section>[-\w]+)/$', 'update_section', name='update_section'),
    url(r'^delete_section/(?P<pk>[-\d]+)/(?P<section>[-\w]+)/$', 'delete_section', name='delete_section'),
    url(r'^change_section_weight/(?P<pk>[-\d]+)/(?P<section>[-\w]+)/(?P<weight>[-\d]+)/$', 'change_section_weight', name='change_section_weight'),
)
