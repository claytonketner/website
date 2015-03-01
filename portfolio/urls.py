from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$',
        'portfolio.views.index',
        name='index'),
    url(r'^blog/(?P<target_blog_slug>[\w\-]+)/$',
        'portfolio.views.blog',
        name='blog'),

    url(r'^admin/', include(admin.site.urls)),
)
