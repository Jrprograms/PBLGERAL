from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .forms import PeopleForm, peopleDeleteForm, SubcategoryForm, SubcategoryDeleteForm
from .models import People, Subcategorie
from .serializer import PeopleSerializer, SubcategorySerializer

# Create your views here.

class PeopleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

class SubcategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subcategorie.objects.all()
    serializer_class = SubcategorySerializer

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
            return redirect('../')
    else:
        form = PeopleForm()
    return render(request, 'create.html', context={'form': form})

def updatePeople(request, people_id):
    people = get_object_or_404(People, pk=people_id)
    if request.method == 'POST':
        form = PeopleForm(request.POST, instance=people)
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form = PeopleForm(instance=people)
    return render(request, 'update.html', context={'form':form})

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

def createSubcategory(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create/../')
    else:
        form = SubcategoryForm()
    return render(request, 'createSubcategory.html', context={'form':form})

def updateSubcategory(request, subcategory_id):
    subcategory = get_object_or_404(Subcategorie, pk=subcategory_id)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('../../../')
    else:
        form = SubcategoryForm(instance=subcategory)
    return render(request, 'updateSubcategory.html', context={'form':form})

def deleteSubcategory(request, subcategory_id):
    subcategory = get_object_or_404(Subcategorie, pk=subcategory_id)
    if request.method == 'POST':
        form = SubcategoryDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            subcategory.delete()
            return redirect('../../../')
    else:
        form = SubcategoryDeleteForm()
    return render(request, 'deleteSubcategory.html', context={'form':form, 'subcategory':subcategory})