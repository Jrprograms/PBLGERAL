from django import forms
from .models import Community, New

class CommunityForm(forms.ModelForm):
    class Meta:
        model =Community 
        fields = ["title","category","foundation_date","visit_time","longitude","latitude","link","logo"]


