from django import forms
from .models import Community, New

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community 
        fields = ['title',
            'category',
            'foundation_date',
            'begin_visit_time',
            'end_visit_time',
            'longitude',
            'latitude',
            'link',
            'logo']
        
        widgets ={
            "title": forms.TextInput(attrs = {'class': 'text-field',}),
            "foundation_date" : forms.DateInput(attrs = {'class': 'text-field','type': 'date'}),
            "end_visit_time" : forms.TimeInput(attrs={'type' : 'time'},format='%H:%M'),
            "begin_visit_time" : forms.TimeInput(attrs={'type' : 'time'},format='%H:%M')
            
        }

    # def __init__(self,*args, **kwargs):
    #     super(CommunityForm,self).__init__(*args, **kwargs)



class CommunityDeleteForm(forms.Form):
    confirm = forms.BooleanField(label="Enviar Deleção")    