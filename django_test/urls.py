from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from .apps.clients.views import CreateClientView, DetailClientView

urlpatterns = patterns('',
    # Examples:

    url(r'^$', CreateClientView.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)$', DetailClientView.as_view(), 
    		name='detail_client')
    # url(r'^django_test/', include('django_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
