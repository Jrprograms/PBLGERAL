from django.db import models

#Events an reviews entities:

class Event(models.Model):

    #test

    title = models.CharField(max_length=100)

    description = models.CharField(max_length=100)
    profile_image = models.ImageField()

    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField()

    adress = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    link = models.URLField()
    value = models.DecimalField(decimal_places=2,max_digits=100)

    pix_key = models.URLField(max_length=100)
    pix_key_owner = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)

    pdf_link = models.URLField(max_length=100)
    questionary_link = models.URLField(max_length=100)
    category = models.CharField(max_length=20, choices="")
    format = models.Choices("Syncron", "Assincron-")
    
    # fk_project = models.ForeignKey(None, on_delete=True)

# class report(models.Model):
#     pass
#    #em construção ;)