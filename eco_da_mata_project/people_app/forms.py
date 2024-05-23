from django import forms 
from .models import People, Subcategorie

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategorie
        fields = ['name', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-select'})
            }

class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['name', 'email', 'description', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-select'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            }

class peopleDeleteForm(forms.Form):
    confirm = forms.BooleanField(label="Confirm deletion")