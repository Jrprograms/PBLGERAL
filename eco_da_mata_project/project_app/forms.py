from django import forms 
from .models import Project

class ProjectForm():
    class meta:
        model = Project
        fields = ['name', 'description', 'email' ,'start_date', 'end_date', 'link', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'start_date': forms.DateField(),
            'end_date': forms.DateField(),
            'link': forms.URLField(),
            'phone_number': forms.IntegerField()
        }