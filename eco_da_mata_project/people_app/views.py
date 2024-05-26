from django.shortcuts import render, get_object_or_404, redirect
from .forms import PeopleForm, peopleDeleteForm
from .models import People

# Create your views here.

def getAllPeoples(request):
    pessoas = People.objects.all()
    return render(request, 'lista.html', context={'parceiros':pessoas})

def getPeople(request, people_id):
    parceiro = get_object_or_404(People, pk=people_id)
    return render(request, 'uniquePeople.html', context={'parceiro': parceiro})

def createPeople(request):
    if request.method == 'POST':
        form = PeopleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createPeople')
    else:
        form = PeopleForm()
    return render(request, 'create.html', context={'form': form})

def deletePeople(request,people_id):
    people = get_object_or_404(People, pk=people_id)
    if request.method == 'POST':
        form = peopleDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            people.delete()
            return redirect('../../')  # Redirecione para a lista de pessoas ou outra página após a exclusão
    else:
        form = peopleDeleteForm()
    return render(request, 'delete.html', context={'form': form, 'people': people})

