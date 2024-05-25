from . import views
from django.urls import path

urlpatterns = [
    path('', views.get_allprojects, name ="projetos"),
    path('<str:Project_ID>/', views.get_project, name='projeto'),
    path('delete/<str:Project_ID>/', views.delete_project, name='Deletando projeto'),
    #path('create/', views.create_project, name='Criando projeto'),
    path('update/<str:Project_ID>/', views.update_project, name='Editando projeto')

]