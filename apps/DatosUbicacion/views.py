from rest_framework import viewsets
from .models import AmbitoTerritorial, Estado, Municipio, Parroquia, Sector, Ubicacion
from .serializers import AmbitoTerritorialSerializer, EstadoSerializer, MunicipioSerializer, ParroquiaSerializer, SectorSerializer, UbicacionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@permission_classes([IsAuthenticated])
class AmbitoTerritorialViewSet(viewsets.ModelViewSet):
    queryset = AmbitoTerritorial.objects.all()
    serializer_class = AmbitoTerritorialSerializer

@permission_classes([IsAuthenticated])
class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

@permission_classes([IsAuthenticated])
class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

@permission_classes([IsAuthenticated])
class ParroquiaViewSet(viewsets.ModelViewSet):
    queryset = Parroquia.objects.all()
    serializer_class = ParroquiaSerializer

@permission_classes([IsAuthenticated])
class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

@permission_classes([IsAuthenticated])
class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
