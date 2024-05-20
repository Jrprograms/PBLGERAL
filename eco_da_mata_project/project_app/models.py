from django.db import models

from community_app.models import Community
from people_app.models import People

# Create your models here.

class Project (models.Model):

    id = models.UUIDField(primary_key=True)
    date = models.DateField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    link = models.URLField(max_length=200)

    phone_number = models.IntegerField() # IntegerField não precisa do max_length. Já removido.
    email = models.EmailField()

    id_people = models.ForeignKey(People, on_delete=models.CASCADE)   
    id_community = models.ForeignKey(Community, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + self.description

     
