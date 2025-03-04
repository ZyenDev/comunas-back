from rest_framework import viewsets
from .models import Comuna, ConsejoComunal
from .serializers import ComunaSerializer, ConsejoComunalSerializer

# Create your views here.

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

class ConsejoComunalViewSet(viewsets.ModelViewSet):
    queryset = ConsejoComunal.objects.all()
    serializer_class = ConsejoComunalSerializer