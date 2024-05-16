from django.db import models
from eco_da_mata_project.community_app.models import Community
from eco_da_mata_project.people_app.models import People
# Create your models here.

class Project (models.Model):

    date = models.DateField()
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    phone_number = models.IntegerField(max_length=11)
    email = models.EmailField()
    id_people = models.ForeignKey(People, on_delete=models.CASCADE)   
    id_community = models.ForeignKey(Community, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

     
