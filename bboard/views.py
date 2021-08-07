from django.http import HttpResponse

from .models import Bd


def index(request):
    s = 'List of data\r\n\r\n\r\n'
    for bb in Bd.objects.order_by('-published'):  # сортировка по убыванию даты публикации
        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')  # задаём тип отправляемых данных и их кодировку
