from django.contrib import admin
from django.db import models
from django.utils import timezone

from pagedown.widgets import AdminPagedownWidget
from adminfiles.admin import FilePickerAdmin

from blog.models import Blog
from blog.models import BlogEntry


class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'when_created', 'views')
    prepopulated_fields = {'slug': ('name', )}

    def save_model(self, request, obj, form, change):
        if not obj.when_created:
            obj.when_created = timezone.now()
        obj.save()


class BlogEntryAdmin(FilePickerAdmin):
    list_display = ('title', 'blog', 'when_created', 'published')
    prepopulated_fields = {'slug': ('title', )}
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
    adminfiles_fields = ('body',)

    def save_model(self, request, obj, form, change):
        if not obj.when_created:
            obj.when_created = timezone.now()
        obj.save()


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogEntry, BlogEntryAdmin)
