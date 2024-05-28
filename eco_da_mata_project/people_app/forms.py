from django import forms 
from .models import People, Subcategorie

CATEGORY_CHOICES = [
    ('PEOPLE', 'Pessoa'),
    ('INTERPRISE', 'Empresa'),
    ]

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategorie
        fields = ['name', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-select'})
            }

class SubcategoryDeleteForm(forms.Form):
    confirm = forms.BooleanField(label='delete subcategory?')

class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['name', 'email', 'description', 'category', 'fk_subcategory']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-select'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            }
    def __init__(self, *args, **kwargs):
        super(PeopleForm, self).__init__(*args, **kwargs)
        self.fields['category'].choices = CATEGORY_CHOICES
        self.fields['fk_subcategory'].queryset = Subcategorie.objects.all()

class peopleDeleteForm(forms.Form):
    confirm = forms.BooleanField(label="Delete people?")