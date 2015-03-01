from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^(?P<target_blog_slug>[\w\-]+)/$',
        'blog.views.blog',
        name='blog'),
    url(r'^admin/',
        include(admin.site.urls)),
)

