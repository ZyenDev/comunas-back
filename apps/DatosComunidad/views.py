from rest_framework import viewsets
from .models import Comuna, ConsejoComunal
from .serializers import ComunaSerializer, ConsejoComunalSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


@permission_classes([IsAuthenticated])
class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer


@permission_classes([IsAuthenticated])
class ConsejoComunalViewSet(viewsets.ModelViewSet):
    queryset = ConsejoComunal.objects.all()
    serializer_class = ConsejoComunalSerializer
