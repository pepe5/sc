from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sc_server.views.home', name='home'),
    # url(r'^sc_server/', include('sc_server.foo.urls')),
    url(r'^polls-stream/', 'sc_server.polls.views.stream_response', name='stream_response'),
    url(r'^polls-tail/', 'sc_server.polls.views.stream_tail', name='stream_tail'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
