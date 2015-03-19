from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shrink.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','manager.views.index'),
    url(r'^(.*)', 'manager.views.redirect'),
    # url(r'^admin/', include(admin.site.urls)),
)
