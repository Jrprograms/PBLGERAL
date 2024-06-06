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
    
    
class NewsForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ["id_community",
            "title",
            "news_text",
            "publish_date",
            "category",
            "link"]
        
        widgets = {
            "id_community": forms.Select(attrs={'class':'select-input'}),
            "title": forms.TextInput(attrs={'class': 'text-field'}),
            "news_text": forms.Textarea(attrs={'class': 'text-field'}),
            "publish_date": forms.DateInput(attrs={'class': 'text-field', 'type': 'date'}),
            "link": forms.URLInput(attrs={'class': 'text-field'}),}
        
    def __init__(self,*args, **kwargs):
        super(NewsForm,self).__init__(*args, **kwargs)
        self.fields['id_community'].queryset = Community.objects.all()

class NewsDeleteForm(forms.Form):
    confirm = forms.BooleanField(label="Enviar Deleção")
    