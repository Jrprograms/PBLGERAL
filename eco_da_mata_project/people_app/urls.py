from django.urls import path
from . import views

urlpatterns = [
    path('list', views.getAllPeoples),
    path('<int:people_id>', views.getPeople),
    path('<int:people_id>/delete/', views.deletePeople),
]
