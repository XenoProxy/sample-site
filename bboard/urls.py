from django.urls import path

from .views import index, by_rubric, BdCreateView

# именнованные маршруты позволяют исп-ать технологию обратного разрешения адресов
urlpatterns = [
    path('add/', BdCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]