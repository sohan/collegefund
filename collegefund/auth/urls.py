from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'collegefund.views.home', name='home'),
    # url(r'^collegefund/', include('collegefund.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'login/$', 'django.contrib.auth.views.login', 
        {'template_name': 'login.html'}),
)
