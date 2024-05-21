from django.shortcuts import render
from .models import Project

# Create your views here.
projetos = Project.objects.all()

def getallprojects(request):
    return render(request, 'projects.html', {'projetos': projetos})

def getproject(request, ID):
     for projeto in projetos:
          if projeto.id == ID:
               return render(request, 'project.html', {'projeto': projeto})