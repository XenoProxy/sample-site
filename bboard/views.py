from django.shortcuts import render

from .models import Bd


def index(request):
    bbs = Bd.objects.order_by('-published')  # сортировка по убыванию даты публикации
    return render(request, 'index.html', {'bbs': bbs})  # загрузка и рендер страницы
