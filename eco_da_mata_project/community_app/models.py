from django.db import models

# Create your models here.


class Community (models.Model):

    category_choices =[
        ("COMMUNITY","Comunidade"),
        ("Tourist attraction","Ponto Turístico")] 
    
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=category_choices)
    foundation_date = models.DateField()
    visit_time = models.TimeField()
    longitude = models.IntegerField()
    latitude = models.IntegerField()
    link = "não sei"

    def __str__(self):
        return self.name

class News (models.Model):

    id = models.IntegerField(primary_key=True)
    id_community = models.ForeignKey(Community, on_delete=models.CASCADE) 
    title = models.CharField(max_length=500)
    news_text = models.TextField()
    publish_date = models.DateField()
    category = "Não lembro"
    link = "não sei"
    
    def __str__(self):
        return self.name
    