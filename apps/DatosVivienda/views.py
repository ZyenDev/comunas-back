from rest_framework import viewsets
from .models import ServiciosBasicos, SituacionVivienda, Telefono, TipoOcupacionVivienda, TipoPared, TipoPiso, TipoTecho, TipoVivienda, Vivienda
from .serializers import ServiciosBasicosSerializer, SituacionViviendaSerializer, TelefonoSerializer, TipoOcupacionViviendaSerializer, TipoParedSerializer, TipoPisoSerializer, TipoTechoSerializer, TipoViviendaSerializer, ViviendaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@permission_classes([IsAuthenticated])
class ServiciosBasicosViewSet(viewsets.ModelViewSet):
    queryset = ServiciosBasicos.objects.all()
    serializer_class = ServiciosBasicosSerializer

@permission_classes([IsAuthenticated])
class SituacionViviendaViewSet(viewsets.ModelViewSet):
    queryset = SituacionVivienda.objects.all()
    serializer_class = SituacionViviendaSerializer

@permission_classes([IsAuthenticated])
class TelefonoViewSet(viewsets.ModelViewSet):
    queryset = Telefono.objects.all()
    serializer_class = TelefonoSerializer

@permission_classes([IsAuthenticated])
class TipoOcupacionViviendaViewSet(viewsets.ModelViewSet):
    queryset = TipoOcupacionVivienda.objects.all()
    serializer_class = TipoOcupacionViviendaSerializer

@permission_classes([IsAuthenticated])
class TipoParedViewSet(viewsets.ModelViewSet):
    queryset = TipoPared.objects.all()
    serializer_class = TipoParedSerializer

@permission_classes([IsAuthenticated])
class TipoPisoViewSet(viewsets.ModelViewSet):
    queryset = TipoPiso.objects.all()
    serializer_class = TipoPisoSerializer

@permission_classes([IsAuthenticated])
class TipoTechoViewSet(viewsets.ModelViewSet):
    queryset = TipoTecho.objects.all()
    serializer_class = TipoTechoSerializer

@permission_classes([IsAuthenticated])
class TipoViviendaViewSet(viewsets.ModelViewSet):
    queryset = TipoVivienda.objects.all()
    serializer_class = TipoViviendaSerializer

@permission_classes([IsAuthenticated])
class ViviendaViewSet(viewsets.ModelViewSet):
    queryset = Vivienda.objects.all()
    serializer_class = ViviendaSerializer
