from django.urls import path
from . import views

urlpatterns = [
    path("", views.RetrieveCommunityView, name="RetrieveCommunityView"),
    path("create/", views.CreateCommunityView, name="CreateCommunityView")
]
