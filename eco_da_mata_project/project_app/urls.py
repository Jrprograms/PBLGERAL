from . import views.py
from django.urls import path

urlpatterns = [
    path('', views.getallprojects, name ="projetos"),
    path('', views.getproject, name='projeto')

]