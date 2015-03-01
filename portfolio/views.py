from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render

from blog.views import blog


def index(request):
    return blog(request)
