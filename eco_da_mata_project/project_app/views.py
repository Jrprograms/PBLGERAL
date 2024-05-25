from django.shortcuts import render
from .models import Project


def get_allprojects(request):
    projetos = Project.objects.all()
    return render(request, 'index_project.html', {'Projetos': projetos})

def get_project(request, ID):
     projeto = Project.objects.filter(pk=ID)
     return render(request, 'index_project.html', {'Projetos': projeto})


def delete_project(request, ID):
     projeto = Project.objects.filter(pk=ID)
     return render(request, 'delete_project.html', {'Projetos': projeto})

# def create_project(request):
#      return render(request, 'create_project.html', {'Projetos': projetos})


def update_project(request, ID):
     projeto = Project.objects.filter(pk=ID)
     return render(request, 'update_project.html', {'Projetos': projeto})
