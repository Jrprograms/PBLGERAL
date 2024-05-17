from django.db import models

CATEGORY_CHOICES = [
    ('PEOPLE', 'Pessoa'),
    ('INTERPRISE', 'Empresa'),
    ]

# Create your models here.
class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
     
    def __str__(self):
        return self.name

class Login(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    # icon = models.models.models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    fk_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    fk_login = models.ForeignKey(Login, on_delete=models.CASCADE)

    def __str__(self):
        return self.name