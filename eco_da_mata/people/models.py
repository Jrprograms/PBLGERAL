from django.db import models

CATEGORY_CHOICES = [
    ('PEOPLE', 'Pessoa'),
    ('INTERPRISE', 'Empresa'),
    ]

# Create your models here.
class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

class Login(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.models.EmailField(max_length=254)

class People(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    # icon = models.models.ImageField() <- não faço ideia de como isso funciona
    category = models.models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    id_people = models.IntegerField(primary_key=True)
    fk_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    fk_login = models.ForeignKey(Login, on_delete=models.CASCADE)