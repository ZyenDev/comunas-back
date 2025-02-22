from rest_framework import viewsets
from .models import ServiciosBasicos, SituacionVivienda, Telefono, TipoOcupacionVivienda, TipoPared, TipoPiso, TipoTecho, TipoVivienda, Vivienda
from .serializers import ServiciosBasicosSerializer, SituacionViviendaSerializer, TelefonoSerializer, TipoOcupacionViviendaSerializer, TipoParedSerializer, TipoPisoSerializer, TipoTechoSerializer, TipoViviendaSerializer, ViviendaSerializer

# Create your views here.

class ServiciosBasicosViewSet(viewsets.ModelViewSet):
    queryset = ServiciosBasicos.objects.all()
    serializer_class = ServiciosBasicosSerializer

class SituacionViviendaViewSet(viewsets.ModelViewSet):
    queryset = SituacionVivienda.objects.all()
    serializer_class = SituacionViviendaSerializer

class TelefonoViewSet(viewsets.ModelViewSet):
    queryset = Telefono.objects.all()
    serializer_class = TelefonoSerializer

class TipoOcupacionViviendaViewSet(viewsets.ModelViewSet):
    queryset = TipoOcupacionVivienda.objects.all()
    serializer_class = TipoOcupacionViviendaSerializer

class TipoParedViewSet(viewsets.ModelViewSet):
    queryset = TipoPared.objects.all()
    serializer_class = TipoParedSerializer

class TipoPisoViewSet(viewsets.ModelViewSet):
    queryset = TipoPiso.objects.all()
    serializer_class = TipoPisoSerializer

class TipoTechoViewSet(viewsets.ModelViewSet):
    queryset = TipoTecho.objects.all()
    serializer_class = TipoTechoSerializer

class TipoViviendaViewSet(viewsets.ModelViewSet):
    queryset = TipoVivienda.objects.all()
    serializer_class = TipoViviendaSerializer

class ViviendaViewSet(viewsets.ModelViewSet):
    queryset = Vivienda.objects.all()
    serializer_class = ViviendaSerializer
