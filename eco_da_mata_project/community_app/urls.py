from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.retrieve_all_community_view, name = "retrieve_all_community_view"), #get all
    path("create/", views.create_community_view, name = "views.create_community_view"), #create
    path("<str:community_id>", views.retrieve_community_view, name = "retrieve_community_view"), #get
    path("delete/", views.delete_community_view, name = "delete_community_view"), #delete
    path("update/", views.delete_community_view, name = "update_community_view") #update
] 