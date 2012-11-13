from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sc_agents.views.home', name='home'),
    url(r'^webui/', 'sc_agents.webui_agent.views.index', name='index'),
    url(r'^stamp/', 'sc_agents.webui_agent.views.stamptime', name='stamptime'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
