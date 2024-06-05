from django.db import models
from community_app.models import Community, New
from events_app.models import Event
from project_app.models import Project

class Image(models.Model):
    
    image = models.ImageField(upload_to = 'images/', null = True)
    category = models.CharField(max_lenght = 50) #incompleta
    link = models.URLField(max_length=200)
    fk_community = models.ForeignKey(Community, on_delete = models.CASCADE)
    fk_event = models.ForeignKey(Event, on_delete = models.CASCADE)
    fk_new = models.ForeignKey(New, on_delete = models.CASCADE)
    fk_project = models.ForeignKey(Project, on_delete = models.CASCADE)
    
# Create your models here.
