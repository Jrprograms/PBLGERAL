from django.shortcuts import render
from .models import People

# Create your views here.

def getPeople(request):
    return render(request, 'html?', {'pessoas': People.objects.all})