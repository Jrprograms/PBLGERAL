from django.db import models
from community_app.models import Community, New
from events_app.models import Event
from project_app.models import Project


class Image(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    link = models.URLField(max_length=200, blank=True) 
    category = models.CharField(max_length=50)
    fk_community = models.ForeignKey(Community, null=True, blank=True, on_delete=models.CASCADE)
    fk_event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.CASCADE)
    fk_project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE)
    fk_new = models.ForeignKey(New, null=True, blank=True, on_delete=models.CASCADE)

# Create your models here.
