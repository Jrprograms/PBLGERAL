from . import views
from django.urls import path

urlpatterns = [
    path('', views.getallprojects, name ="projetos"),
    path('<str:slug>/', views.getproject, name='name_url'),
    path('delete/', views.delproject, name='')

]