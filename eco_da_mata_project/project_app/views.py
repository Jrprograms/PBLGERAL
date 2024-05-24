from django.shortcuts import render
from .models import Project


def get_allprojects(request):
    projetos = Project.objects.all()
    return render(request, 'project.html', {'Projetos': projetos})

def get_project(request, ID):
     projeto = Project.objects.filter(pk=ID)
     return render(request, 'project.html', {'Projetos': projeto})


def delete_project(request, ID):
     return render(request, 'delete.html', {'Projetos': projetos})

def create_project(request):
     return render(request, 'project.html', {'Projetos': projetos})


def update_project(request, ID):
     return render(request, 'project.html', {'Projetos': projetos})
