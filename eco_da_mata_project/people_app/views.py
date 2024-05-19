from django.shortcuts import render
from .models import People

# Create your views here.

def getPeople(request):
    return render(request, 'index.html', {'pessoas': People.objects.all})