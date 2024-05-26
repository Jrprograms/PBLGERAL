from django.db import models
import random
#Events an reviews entities:

class Event(models.Model):

    id = random.randint(0, 999)#test
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=300)
    profile_image = models.ImageField()
    #__

    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField()
    adress = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    #__

    link = models.URLField(unique=True)
    value = models.DecimalField(decimal_places=2,max_digits=10)
    pix_key = models.URLField(max_length=100) 
    pix_key_owner = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    #__

    pdf_link = models.URLField(max_length=100)
    questionary_link = models.URLField(max_length=100)
    #--
    category = models.CharField(max_length=20 ,choices =[
    ("F", "Feira"),
    ("Ft", "Festividade"),
    ("Cl", "Celebração")    
    ])
    format = models.CharField(max_length=20 ,choices =[
    ("P", "Presencial"),
    ("V", "Virtual"),
    ("H", "Híbrido")
    ])
    #__
    
    # fk_project = models.ForeignKey(None, on_delete=True)

class review(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    grade = models.CharField(max_length=20 ,choices=[
        ("R", "Ruim"),
        ("B", "Bom"),
        ("Mb", "Muito bom")
    ])