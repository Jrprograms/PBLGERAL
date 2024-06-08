from rest_framework import viewsets
from .models import People, Subcategorie
from .serializer import PeopleSerializer, SubcategorySerializer

# Create your views here.

class PeopleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

class SubcategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subcategorie.objects.all()
    serializer_class = SubcategorySerializer
