from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',

    # Auth
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),

    # Settings
    url(r'^settings/(?P<pk>[-\d]+)/$',
        views.SiteSettingsView.as_view(), name='settings'),
    url(r'^update_settings/(?P<pk>[-\d]+)/$',
        views.UpdateSiteSettings.as_view(), name='update_settings'),

    # Pages
    url(r'^$', views.PagesView.as_view(), name='pages'),
    url(r'^pages/$', views.PagesView.as_view(), name='pages'),
    url(r'^create_page/$', views.CreatePage.as_view(), name='create_page'),
    url(r'^update_page/(?P<pk>[-\d]+)/$',
        views.UpdatePage.as_view(), name='update_page'),
    url(r'^delete_page/(?P<pk>[-\d]+)/$',
        views.DeletePage.as_view(), name='delete_page'),

    url(r'^set_page_weight/(?P<pk>[-\d]+)/(?P<weight>[-\d]+)/$',
        views.SetPageWeight.as_view(), name='set_page_weight'),

    # Sections
    url(r'^create_section/(?P<page_pk>[-\d]+)/(?P<section>[-\w]+)/$',
        views.CreateSection.as_view(), name='create_section'),
    url(r'^update_section/(?P<pk>[-\d]+)/(?P<section>[-\w]+)/$',
        views.UpdateSection.as_view(), name='update_section'),
    url(r'^delete_section/(?P<pk>[-\d]+)/(?P<section>[-\w]+)/$',
        views.DeleteSection.as_view(), name='delete_section'),

    url(r'^set_section_weight/(?P<pk>[-\d]+)/(?P<section>[-\w]+)/(?P<weight>[-\d]+)/$',
        views.SetSectionWeight.as_view(), name='set_section_weight'),
)
