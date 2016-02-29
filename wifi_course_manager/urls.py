from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # auth
    url('^', include('django.contrib.auth.urls')),

    # admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # apps
    url(r'^fetch/', include('fetch.urls')),
    url(r'^', include('display.urls')),
)
