from django.shortcuts import render, get_object_or_404, redirect
from .models import * 
from . import forms
from rest_framework import viewsets
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

def get_allprojects(request):
    projects = Project.objects.all()
    return render(request, 'index_projects.html', context={'Projects': projects})

def get_project(request, Project_ID):
    project = get_object_or_404(Project, id=Project_ID)
    return render(request, 'index_project.html', context={'Project': project})

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
    project = get_object_or_404(Project, pk=Project_ID)
    if request.method == 'PUT':
        form = forms.ProjectForm(request.PUT)
        if form.is_valid():
            form.save()
            return redirect('../../')
    else:
        form = forms.ProjectForm()
    return render(request, 'update_project.html', context={'Project': project})

