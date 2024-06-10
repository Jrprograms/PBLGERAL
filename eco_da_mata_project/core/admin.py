from django.contrib import admin
from .models import Imagem
from community_app.models import Community
from community_app.models import News
from events_app.models import Event 
from people_app.models import People
from project_app.models import Project 

# Register your models here.

class Imagemnline(admin.TabularInline):
    model = Imagem
    extra = 1

class CommunityAdmin(admin.ModelAdmin):
    inlines = [ImagemInline]

class NewAdmin(admin.ModelAdmin):
    inlines = [ImagemInline]


admin.site.register(Community, CommunityAdmin)
admin.site.register(New, NewAdmin)

