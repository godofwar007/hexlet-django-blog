from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    app_name = 'articleeeee'
    return render(request, 'articles/index.html', context={
        'name': app_name,
    })
