from django import template

register = template.Library()


@register.filter
def fix_upload_paths(arg):
    return arg.replace('portfolio/site_media/uploads',
                       'portfolio/static/uploads')
