from django.db import models

# Create your models here.

class Event(models.Model):

    title = models.CharField(max_length=100)

    description = models.CharField(max_length=100)
    profile_image = models.ImageField()

    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField()

    adress = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    link = models.CharField(max_length=100)
    value = models.DecimalField()

    pix_key = models.CharField(max_length=500)
    pix_key_owner = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)

    pdf_link = models.CharField(max_length=300)
    questionary_link = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices="")
    
    fk_project = models.ForeignKey(None, on_delete=True)
    fk_image = models.ForeignKey(None, on_delete=True)

class report(models.Model):
   #em construção ;)