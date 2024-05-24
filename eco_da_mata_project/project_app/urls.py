from . import views
from django.urls import path

urlpatterns = [
    path('', views.get_allprojects, name ="projetos"),
    path('<str:id>/', views.get_project, name='projeto'),
    path('delete/<str:id>/', views.delete_project, name='Deletando projeto'),
    path('create/', views.create_project, name='Criando projeto'),
    path('update/<str:id>/', views.update_project, name='Editando projeto')

]