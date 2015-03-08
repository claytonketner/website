from django import template

register = template.Library()

@register.filter
def print_out(stuff):
    print stuff
    return stuff
