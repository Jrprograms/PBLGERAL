from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from community_app.views import CommunityViewSet, NewViewSet 
from people_app.views import PeopleViewSet
from project_app.views import ProjectViewSet
from events_app.views import EventViewSet

Router = DefaultRouter()
Router.register('community', CommunityViewSet)
Router.register('new', NewViewSet)
Router.register('people', PeopleViewSet)
Router.register('project', ProjectViewSet)
Router.register('events', EventViewSet)


schena_view = get_schema_view(
    openapi.Info(
        title="Eco da Mata",
        default_version='v1',
        description='Sem descrição',
        terms_of_service="https://www.community.com/terms/",
        contact=openapi.Contact(),
        license=openapi.License(name="Sem nome"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

#É uma boa prática nomear os paths de vocês. Principalmente quando tiverem trabalhando com formulários.
urlpatterns = [
    path('swagger<format>/', schena_view.without_ui(cache_timeout=0), name='schena-json'),
    path('swagger/', schena_view.with_ui('swagger', cache_timeout=0), name='schena-swagger-ui'),
    path('redoc/', schena_view.with_ui('redoc', cache_timeout=0), name='schena-redoc'),
    path('api/', include(Router.urls)),
    path('community/', include('community_app.urls')), 
    path('project/', include('project_app.urls'))
]

    # path('admin/', admin.site.urls),
    # path('community/', include('community_app.urls')),
    # path('parceiros/', include('people_app.urls')),
    # path('projeto/', include('project_app.urls')),
    # path('events/', include('events_app.urls'))


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
