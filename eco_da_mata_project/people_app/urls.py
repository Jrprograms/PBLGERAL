from django.urls import path
from . import views

urlpatterns = [
    path('All', views.getAllPeoples, name='Parceiros'),
    path('All/<str:name>', views.getPeople, name='Adicionar_parceiro')
]
