from django.contrib import admin
from .models import Image
from community_app.models import Community, New
from events_app.models import Event 
from people_app.models import People
from project_app.models import Project 

class ImagemInline(admin.TabularInline):
    model = Image
    extra = 1

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'category', 'link', 'fk_community')  
    search_fields = ['category'] 

admin.site.register(Image, ImageAdmin) 

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    inlines = [ImagemInline]

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    inlines = [ImagemInline]

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [ImagemInline]
