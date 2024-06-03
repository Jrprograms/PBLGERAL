from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("create/", views.create_event, name = "create_event"),
    path("list/", views.get_events, name = "get_events"),
    path("<uuid:event_id>", views.get_single_event , name = "get_single_event"),
    path('edit/<uuid:event_id>/', views.edit_event, name='edit_event'),
    path('delete/<uuid:event_id>/', views.delete_event, name='delete_event'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
