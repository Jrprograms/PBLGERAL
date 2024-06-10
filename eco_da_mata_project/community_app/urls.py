from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


router


urlpatterns = [
    path("", views.retrieve_all_community_view, name = "retrieve_all_community_view"),                #get all
    path("create/", views.create_community_view, name = "create_community_view"),                     #create
    path("<str:community_id>", views.retrieve_community_view, name = "retrieve_community_view"),      #get
    path("<str:community_id>/delete/", views.delete_community_view, name = "delete_community_view"),  #delete
    path("<str:community_id>/update/", views.update_community_view, name = "update_community_view"),  #update
    
    path("news/", views.retrieve_all_news_view, name = "retrieve_all_news_view"),          #get all
    path("news/create/", views.create_news_view, name = "create_news_view"),               #create
    path("news/<str:news_id>", views.retrieve_news_view, name = "retrieve_news_view"),     #get
    path("news/<str:news_id>/delete/", views.delete_news_view, name = "delete_news_view"), #delete
    path("news/<str:news_id>/update/", views.update_news_view, name = "update_news_view")  #update
]