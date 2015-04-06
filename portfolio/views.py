from django.http import HttpResponse
from django.shortcuts import redirect, render

from blog.views import blog


def index(request):
    return blog(request)
