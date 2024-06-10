from django.contrib.auth.models import User
from django.db import models

CATEGORY_CHOICES = [
    ('PEOPLE', 'Pessoa'),
    ('INTERPRISE', 'Empresa'),
    ]

# Create your models here.
class Subcategorie(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    id = models.AutoField(primary_key=True)
     
    def __str__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=False, default='example@example.com')
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    fk_subcategory = models.ForeignKey(Subcategorie, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='photos/', null=True)
    link = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.name.username