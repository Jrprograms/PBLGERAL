from django.shortcuts import render
from .models import Project

# Create your views here.
projetos = Project.objects.all()

def getallprojects(request):
    projetos = Project.objects.all()
    return render(request, 'projects.html', {'projetos': projetos})

def getproject(request, ID):
     projeto = Project.objects.filter(pk=ID)
     return render(request, 'project.html', {'projeto': projeto})