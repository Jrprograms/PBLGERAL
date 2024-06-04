from rest_framework import serializers
from .models import People,Subcategorie

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategorie
        fields = '__all__'