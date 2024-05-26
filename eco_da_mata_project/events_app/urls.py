from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("create/", views.create_event, name = "create_event"),
    path("list/", views.get_events, name = "get_events"),
    path("<int:event_id>", views.get_single_event , name = "get_single_event"),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
] 