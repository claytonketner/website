from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    context['message'] = "I'm switching this site to Django in " \
                         "my free time. It might take a while!"
    return render(request, 'portfolio/index.html', context)
