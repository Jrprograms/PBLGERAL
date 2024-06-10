from rest_framework.viewsets import ModelViewSet
from .models import Community, News
from .serializers import CommunitySerializer, NewSerializer


class CommunityViewSet(ModelViewSet)
    queryset = Communtiy.objects.all()
    serializer_class = CommunitySerializer

class NewViewSet(ModelViewSet)
    queryset = New.objects.all()
    serializer_class = NewSerializer