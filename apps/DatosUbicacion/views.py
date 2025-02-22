from rest_framework import viewsets
from .models import AmbitoTerritorial, Estado, Municipio, Parroquia, Sector, Ubicacion
from .serializers import AmbitoTerritorialSerializer, EstadoSerializer, MunicipioSerializer, ParroquiaSerializer, SectorSerializer, UbicacionSerializer

# Create your views here.

class AmbitoTerritorialViewSet(viewsets.ModelViewSet):
    queryset = AmbitoTerritorial.objects.all()
    serializer_class = AmbitoTerritorialSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    
class ParroquiaViewSet(viewsets.ModelViewSet):
    queryset = Parroquia.objects.all()
    serializer_class = ParroquiaSerializer

class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
