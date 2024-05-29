from django.db import models
import uuid

#Events an reviews entities:

class Event(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True, editable=False)
    title = models.CharField(max_length=50, verbose_name="Título")
    body = models.CharField(max_length=300, verbose_name="Descrição")
    profile_image = models.ImageField(upload_to="media/events/", verbose_name="Imagem de perfil")
    #__

    begin_date = models.DateField(verbose_name="Data de início")
    end_date = models.DateField(verbose_name="Data de fim")
    time = models.TimeField(verbose_name="Horário")
    address = models.CharField(max_length=100, verbose_name="Endereço")
    location = models.CharField(max_length=100, verbose_name="Localização")
    #__

    link = models.URLField(verbose_name="Link")
    value = models.DecimalField(decimal_places=2,max_digits=10, verbose_name="Valor")
    pix_key = models.URLField(max_length=100, verbose_name="Chave PIX") 
    pix_key_owner = models.CharField(max_length=100, verbose_name="Dono da chave PIX")
    bank_name = models.CharField(max_length=100, verbose_name="Banco")
    #__

    pdf_link = models.URLField(max_length=100, null=True, verbose_name="Link para PDF")
    questionary_link = models.URLField(max_length=100, null=True, verbose_name="Link para questionário")
    #--
    category = models.CharField(max_length=20,default="Vazio" ,choices =[
    ("F", "Feira"),
    ("Ft", "Festividade"),
    ("Cl", "Celebração")    
    ])
    format = models.CharField(max_length=20, default="Vazio" ,choices =[
    ("P", "Presencial"),
    ("V", "Virtual"),
    ("H", "Híbrido")
    ])
    #__
    
    # fk_project = models.ForeignKey(None, on_delete=True)

class review(models.Model):
    title = models.CharField(max_length=50,verbose_name="Título")
    body = models.CharField(max_length=300, verbose_name="Mensagem")
    author = models.CharField(max_length=100)
    grade = models.CharField(max_length=20 ,choices=[
    ("R", "Ruim"),
    ("B", "Bom"),
    ("Mb", "Muito bom")
    ], verbose_name="Avaliação")