from django import forms
from .models import event, review

class event_form(forms.ModelForm):
    class Meta:
        model = event
        fields = ["title","body","profile_image","start_date","end_date","time","adress","location",
                  "link", "value", "pix_key", "pix_key_owner", "bank_name", "pdf_link", "questionary_link",
                  "category", "format"]
