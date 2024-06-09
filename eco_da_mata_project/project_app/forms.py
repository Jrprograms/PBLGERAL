from django import forms 
from .models import Project
from django.db import models

import uuid
from community_app.models import Community
from people_app.models import People

class ProjectForm():
    class meta:
        model = Project
        fields = ['id','name', 'description', 'email' , 'link', 'phone_number']
        widgets = {
            'id': models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'link': forms.URLField(),
            'phone_number': forms.IntegerField()
        }
