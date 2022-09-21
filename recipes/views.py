from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'benjamin zerpa',        
    }) 


def contato(request):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')
