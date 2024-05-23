from django import forms 
from .models import People, Subcategorie

class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['name', 'email', 'description', 'category']

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategorie
        fields = ['nome', 'categoria']