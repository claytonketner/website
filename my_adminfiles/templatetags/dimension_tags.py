from django import template
from django.conf import settings


register = template.Library()


@register.filter
def trim_width(upload):
    width = upload.width()
    if width > 800:
        return 800
    return width


@register.filter
def trim_height(upload):
    trimmed_width = trim_width(upload)
    width = upload.width()
    height = upload.height()
    percent_scale = float(trimmed_width) / width
    return int(height * percent_scale)


@register.filter
def fix_url(url):
    return settings.HOST + url
