from django.conf.urls import patterns, include, url
import entries.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('entries.views',
    url(r'^$', 'home'),
    url(r'^post/$', 'post'),
    url(r'^saved/$', 'saved'),
    url(r'^saved_true/(?P<ad_id>\d+)/$', 'saved_true'),
    url(r'^posted/$', 'posted'),
    url(r'^entry/(?P<ad_id>\d+)/$', 'entry'),
    url(r'^textbooks/$', 'textbooks'),
    url(r'^bikes/$', 'bikes'),
    url(r'^admin/', include(admin.site.urls)),
)
