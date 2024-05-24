from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("create/", views.create_event, name = "create_event"),
    path("list/", views.getEvents, name = "getEvents"),
] 