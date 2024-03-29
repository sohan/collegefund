from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('fund.views',
    # Examples:
    # url(r'^$', 'collegefund.views.home', name='home'),
    # url(r'^collegefund/', include('collegefund.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'admin/', include(admin.site.urls)),
    url(r'about$', 'about'),
    url(r'students$', 'students'),
    url(r'donors$', 'donors'),
    url(r'facts$', 'facts'),
    url(r'faq$', 'faq'),
    url(r'privacy$', 'privacy_policy'),
    url(r'$', 'index'),
)
