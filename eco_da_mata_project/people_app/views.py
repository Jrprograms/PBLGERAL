from django.shortcuts import render, get_object_or_404
from .models import People

# Create your views here.

def getAllPeoples(request):
    pessoas = People.objects.all()
    return render(request, 'index.html', context={'parceiros':pessoas})

def getPeople(request, people_id): # Corrigir essa bomba
    parceiro = get_object_or_404(People, pk=people_id)
    return render(request, 'unique.html', context={'parceiro': parceiro})


def createPeople(request):
    pass

def updatePeople(request):
    pass

def deletePeople(request):
    pass