from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from . import forms

def get_allprojects(request):
    projetos = Project.objects.all()
    return render(request, 'index_projects.html', context={'Projetos': projetos})

def get_project(request, Project_ID):
     projeto = get_object_or_404(Project, id=Project_ID)
     return render(request, 'index_project.html', context={'Projeto': projeto})


def delete_project(request, Project_ID):
     pass

def create_project(request):
     if request.method == 'post':
        form = forms.ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'')
     else:
        form = forms.ProjectForm()
        contexto = {'form': form}
        return render(request, 'create_project.html', context=contexto)


def update_project(request, Project_ID):
     pass
