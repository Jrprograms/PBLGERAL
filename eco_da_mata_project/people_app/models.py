from django.contrib.auth.models import User
from django.db import models

CATEGORY_CHOICES = [
    ('PEOPLE', 'Pessoa'),
    ('INTERPRISE', 'Empresa'),
    ]

# Create your models here.
class Subcategorie(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
     
    def __str__(self):
        return self.name

class People(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    # icon = models.models.models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    fk_subcategory = models.ForeignKey(Subcategorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name