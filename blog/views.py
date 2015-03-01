from django.db.models import F
from django.shortcuts import render

from blog.models import Blog


def blog(request, target_blog_slug=None):
    target_blog = Blog.objects.get(is_index=True)
    if target_blog_slug:
        target_blog = Blog.objects.get(slug=target_blog_slug)

    target_blog.views = F('views') + 1
    target_blog.save()
    blog_entries = target_blog.blogentry_set.all()
    blogs = Blog.objects.all()
    context = {
        'current_blog': target_blog,
        'blog_entries': blog_entries,
        'blogs': blogs,
    }
    return render(request, 'portfolio/blog.html', context)
