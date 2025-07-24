from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Nacionalidad, NivelEstudio, PaisOrigen, Celular, CorreoElectronico, EstadoCivil, Etnia, TipoDiscapacidad, TipoSangre, Habitante, HabitanteDiscapacidad, HabitanteEstadoCivil, HabitanteEtnia, HabitanteNivelEstudio, HabitanteTipoSangre
from .serializers import NacionalidadSerializer, NivelEstudioSerializer, PaisOrigenSerializer, CelularSerializer, CorreoElectronicoSerializer, EstadoCivilSerializer, EtniaSerializer, TipoDiscapacidadSerializer, TipoSangreSerializer, HabitanteSerializer, HabitanteDiscapacidadSerializer, HabitanteEstadoCivilSerializer, HabitanteEtniaSerializer, HabitanteNivelEstudioSerializer, HabitanteTipoSangreSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@permission_classes([IsAuthenticated])
class NacionalidadViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer

@permission_classes([IsAuthenticated])
class NivelEstudioViewSet(viewsets.ModelViewSet):
    queryset = NivelEstudio.objects.all()
    serializer_class = NivelEstudioSerializer

@permission_classes([IsAuthenticated])
class PaisOrigenViewSet(viewsets.ModelViewSet):
    queryset = PaisOrigen.objects.all()
    serializer_class = PaisOrigenSerializer

@permission_classes([IsAuthenticated])
class CelularViewSet(viewsets.ModelViewSet):
    queryset = Celular.objects.all()
    serializer_class = CelularSerializer

@permission_classes([IsAuthenticated])
class CorreoElectronicoViewSet(viewsets.ModelViewSet):
    queryset = CorreoElectronico.objects.all()
    serializer_class = CorreoElectronicoSerializer

@permission_classes([IsAuthenticated])
class EstadoCivilViewSet(viewsets.ModelViewSet):
    queryset = EstadoCivil.objects.all()
    serializer_class = EstadoCivilSerializer

@permission_classes([IsAuthenticated])
class EtniaViewSet(viewsets.ModelViewSet):
    queryset = Etnia.objects.all()
    serializer_class = EtniaSerializer

@permission_classes([IsAuthenticated])
class TipoDiscapacidadViewSet(viewsets.ModelViewSet):
    queryset = TipoDiscapacidad.objects.all()
    serializer_class = TipoDiscapacidadSerializer

@permission_classes([IsAuthenticated])
class TipoSangreViewSet(viewsets.ModelViewSet):
    queryset = TipoSangre.objects.all()
    serializer_class = TipoSangreSerializer

@permission_classes([IsAuthenticated])
class HabitanteViewSet(viewsets.ModelViewSet):
    queryset = Habitante.objects.all()
    serializer_class = HabitanteSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        habitante = self.get_object()
        if not hasattr(habitante, 'habitantediscapacidad'):
            tipo_discapacidad_default = TipoDiscapacidad.objects.first()
            HabitanteDiscapacidad.objects.create(
                id_habitante=habitante,
                id_tipo_discapacidad=tipo_discapacidad_default  # Usa un valor válido
            )
        return response

@permission_classes([IsAuthenticated])
class HabitanteDiscapacidadViewSet(viewsets.ModelViewSet):
    queryset = HabitanteDiscapacidad.objects.all()
    serializer_class = HabitanteDiscapacidadSerializer

class HabitanteEstadoCivilViewSet(viewsets.ModelViewSet):
    queryset = HabitanteEstadoCivil.objects.all()
    serializer_class = HabitanteEstadoCivilSerializer

@permission_classes([IsAuthenticated])
class HabitanteEtniaViewSet(viewsets.ModelViewSet):
    queryset = HabitanteEtnia.objects.all()
    serializer_class = HabitanteEtniaSerializer

@permission_classes([IsAuthenticated])
class HabitanteNivelEstudioViewSet(viewsets.ModelViewSet):
    queryset = HabitanteNivelEstudio.objects.all()
    serializer_class = HabitanteNivelEstudioSerializer

@permission_classes([IsAuthenticated])
class HabitanteTipoSangreViewSet(viewsets.ModelViewSet):
    queryset = HabitanteTipoSangre.objects.all()
    serializer_class = HabitanteTipoSangreSerializer

# Busqueda de buscar Habitante por ID de vivienda.

class HabitantesPorViviendaView(APIView):
    def get(self, request, id_vivienda):
        try:
            habitantes = Habitante.objects.filter(id_vivienda=id_vivienda)
            serializer = HabitanteSerializer(habitantes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Habitante.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)