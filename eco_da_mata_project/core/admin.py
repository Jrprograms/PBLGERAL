from django.contrib import admin
from .models import Image
from community_app.models import Community, New
from events_app.models import Event 
from people_app.models import People
from project_app.models import Project 

# Register your models here.

class ImagemInline(admin.TabularInline):
    model = Image
    extra = 1

class CommunityAdmin(admin.ModelAdmin):
    inlines = [ImagemInline]

class NewAdmin(admin.ModelAdmin):
    inlines = [ImagemInline]


admin.site.register(Community, CommunityAdmin)
admin.site.register(New, NewAdmin)

