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
     
    def __str__(self):
        return self.name

class People(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=False, blank=False, max_length=200, default='example@example.com')
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    fk_subcategory = models.ForeignKey(Subcategorie, on_delete=models.CASCADE)
    id = models.IntegerField(auto_created=True, null=False, blank=False, primary_key=True)

    def __str__(self):
        return self.name.username