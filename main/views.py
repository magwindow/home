from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'HOME - Главная',
        'content': 'Магазин мебели HOME',
    }
    
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'HOME - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том почему этот магазин такой классный и какой хороший товар'
    }
    
    return render(request, 'main/about.html', context)
