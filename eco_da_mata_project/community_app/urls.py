from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.retrieve_all_community_view, name = "retrieve_all_community_view"),
    path("create/", views.create_community_view, name = "views.create_community_view"),
    path("<str:community_id>", views.retrieve_community_view, name = "retrieve_community_view")

] 