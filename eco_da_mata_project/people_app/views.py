from django.shortcuts import render
from .models import People

# Create your views here.

def getPeople(request):
    pessoas = People.objects.all()
    return render(request, 'people.html', {'pessoas':pessoas})