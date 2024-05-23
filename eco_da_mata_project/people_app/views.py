from django.shortcuts import render, get_object_or_404, redirect
from . import forms
from .models import People

# Create your views here.

def getAllPeoples(request):
    pessoas = People.objects.all()
    return render(request, 'index.html', context={'parceiros':pessoas})

def getPeople(request, people_id): # Corrigir essa bomba
    parceiro = get_object_or_404(People, pk=people_id)
    return render(request, 'unique.html', context={'parceiro': parceiro})

def createPeople(request): # corrigir também
    if request.method == 'POST':
        form = forms.PeopleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createPeople')
    else:
        form = forms.PeopleForm()
        return render(request, 'create.html', {'form': form})

def deletePeople(request,people_id): # e aqui
    person = get_object_or_404(People, id=people_id)
    if request.method == 'POST':
        form = forms.peopleDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            person.delete()
            return redirect('person_list')  # Redirecione para a lista de pessoas ou outra página após a exclusão
    else:
        form = forms.peopleDeleteForm()
    return render(request, 'delete.html', {'form': form, 'person': person})