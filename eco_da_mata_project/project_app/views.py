from django.shortcuts import render, get_object_or_404
from .models import Project


def get_allprojects(request):
    projetos = Project.objects.all()
    return render(request, 'index_projects.html', context={'Projetos': projetos})

def get_project(request, Project_ID):
     projeto = get_object_or_404(Project, id=Project_ID)
     return render(request, 'index_project.html', context={'Projeto': projeto})


def delete_project(request, Project_ID):
     projeto = Project.objects.filter(pk=Project_ID)
     return render(request, 'delete_project.html', context={'Projetos': projeto})

# def create_project(request):
#      return render(request, 'create_project.html', {'Projetos': projetos})


def update_project(request, Project_ID):
     projeto = Project.objects.filter(pk=Project_ID)
     return render(request, 'update_project.html', {'Projetos': projeto})
