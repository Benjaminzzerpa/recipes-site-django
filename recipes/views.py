from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'benjamin zerpa',       
    }) 


def recipe(request, id):
    return render(request, 'recipes/pages/recipe_view.html', context={
        'name': 'benjamin zerpa',       
    }) 



