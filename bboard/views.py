from django.shortcuts import render

from .models import Bd


def index(request):
    bbs = Bd.objects.all()
    return render(request, 'index.html', {'bbs': bbs})  # загрузка и рендер страницы
