from rest_framework import viewsets
from .models import People, Subcategorie
from .serializer import PeopleSerializer, SubcategorySerializer

class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer()

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategorie.objects.all()
    serializer_class = SubcategorySerializer()