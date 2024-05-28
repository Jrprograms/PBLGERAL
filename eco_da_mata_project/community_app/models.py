from django.db import models
import uuid
# Create your models here.

class Community (models.Model):

    category_choices =[   
        ("COMMUNITY","Comunidade"),
        ("Tourist attraction","Ponto Turístico")] 
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=category_choices)
    foundation_date = models.DateField()
    visit_time = models.TimeField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    link = models.URLField(max_length=200)
    logo = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title + " " + self.category

class New(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_community = models.ForeignKey(Community, on_delete=models.CASCADE) 
    title = models.CharField(max_length=500)
    news_text = models.TextField()
    publish_date = models.DateField()
    category = models.CharField(max_length=100)
    link = models.URLField()
    
    def __str__(self):
        return self.title
