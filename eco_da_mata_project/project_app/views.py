from django.shortcuts import render
from .models import Project

#gets

def getallprojects(request):
    projetos = Project.objects.all()
    return render(request, 'project.html', {'projetos': projetos})

def getproject(request, ID):
     projeto = Project.objects.filter(pk=int(ID))
     return render(request, 'project.html', {'projeto': projeto})


