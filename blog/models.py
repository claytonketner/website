from django.db import models
from django.utils import timezone


class Blog(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    is_index = models.BooleanField(default=False)
    when_created = models.DateTimeField(
        blank=True, null=True, help_text="If blank, current time will be used")
    views = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return self.name


class BlogEntry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    slug = models.SlugField(max_length=50, unique=True)
    blog = models.ForeignKey('Blog')
    published = models.BooleanField(default=True)
    when_created = models.DateTimeField(
        blank=True, null=True, help_text="If blank, current time will be used")
    when_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog Entry'
        verbose_name_plural = 'Blog Entries'
        ordering = ['when_created']
