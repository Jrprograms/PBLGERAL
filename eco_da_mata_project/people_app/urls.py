from django.urls import path
from . import views

urlpatterns = [
    path('parceiros/', views.getPeople, name='Parceiros')
]
