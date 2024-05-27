from django import forms
from .models import Event, review

class event_form(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title","body","profile_image","begin_date","end_date","time","address","location",
                  "link", "value", "pix_key", "pix_key_owner", "bank_name", "pdf_link", "questionary_link",
                  "category", "format"]

class deleteeventform(forms.ModelForm):
    delete = forms.IntegerField(label="Deletar Evento:")
    