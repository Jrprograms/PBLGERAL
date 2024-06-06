from django.db import models
import uuid
# Create your models here.

class Community (models.Model):

    category_choices =[   
        ("COMMUNITY","Comunidade"),
        ("Tourist attraction","Ponto Turístico")] 
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, verbose_name="Título")
    category = models.CharField(max_length=50, choices = category_choices, verbose_name="Categoria")
    foundation_date = models.DateField(verbose_name="Data de Fundação")
    begin_visit_time = models.TimeField(verbose_name="Hora de Início da Visita")
    end_visit_time = models.TimeField(verbose_name="Hora de Fim da Visita")
    longitude = models.FloatField(verbose_name="Longitude")
    latitude = models.FloatField(verbose_name="Latitude")
    link = models.URLField(max_length=200, verbose_name="Link")
    logo = models.ImageField(upload_to="images/", verbose_name="Logotipo")

    def __str__(self):
        return self.title

class New(models.Model):
    

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_community = models.ForeignKey(Community, on_delete=models.CASCADE, verbose_name="Comunidade")
    title = models.CharField(max_length=500, verbose_name="Título")
    news_text = models.TextField(verbose_name="Texto da Notícia")
    publish_date = models.DateField(verbose_name="Data de Publicação")
    category = models.CharField(max_length=100, verbose_name="Categoria") 
    link = models.URLField(verbose_name="Link")
    
    def __str__(self):
        return self.title 

