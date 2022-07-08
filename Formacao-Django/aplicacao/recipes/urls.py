from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #informando que vai receber um valor a mais
    path('<int:receita_id>', views.receita, name='receita')
]