from django.shortcuts import render
from .models import People

# Create your views here.

def getPeople(request):
    pessoas = People.objects.all()
    return render(request, 'ListPeoples.html', {'pessoas':pessoas})

def createPeople(request):
    pass

def updatePeople(request):
    pass

def deletePeople(request):
    pass