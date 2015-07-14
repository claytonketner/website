from django import template
from django.conf import settings

register = template.Library()


@register.filter
def fix_upload_paths(arg):
    return arg.replace('/uploads/', settings.STATIC_URL)
