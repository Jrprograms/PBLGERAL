from django.urls import path
from . import views

urlpatterns = [
    path("", views.RetrieveCommunityView),
    path("create/", views.CreateCommunityView)
]
