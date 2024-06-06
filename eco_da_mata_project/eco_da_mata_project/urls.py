from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from community_app.views import CommunityViewSet
from people_app.views import PeopleViewSet
from project_app.views import ProjectViewSet
from events_app.views import EventViewSet

Router = DefaultRouter()
Router.register('community', CommunityViewSet)
Router.register('parceitos', PeopleViewSet)
Router.register('projeto', ProjectViewSet)
Router.register('events', EventViewSet)

#É uma boa prática nomear os paths de vocês. Principalmente quando tiverem trabalhando com formulários.
urlpatterns = [
    path('api/', include(Router.urls))
]

    # path('admin/', admin.site.urls),
    # path('community/', include('community_app.urls')),
    # path('parceiros/', include('people_app.urls')),
    # path('projeto/', include('project_app.urls')),
    # path('events/', include('events_app.urls'))


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)