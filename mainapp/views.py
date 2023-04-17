from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'mainapp/index.html', data )

def about(request):
    data = {
        'title': 'О нас'
    }
    return render(request, 'mainapp/about.html', data)

def contact(request):
    data = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', data)