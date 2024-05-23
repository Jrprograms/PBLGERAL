from django.urls import path
from . import views

urlpatterns = [
    path('list', views.getAllPeoples),
    path('<str:name>', views.getPeople),
    path('<str:name>/delete/', views.deletePeople),
]
