from django.shortcuts import render
from .models import Project
# Create your views here.

def getallprojects(request):
    projetos = Project.objects.all()
    return render(request, 'project.html', {'projetos': projetos})
