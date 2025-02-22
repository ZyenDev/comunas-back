from rest_framework import viewsets
from .models import Nacionalidad, NivelEstudio, PaisOrigen, Celular, CorreoElectronico, EstadoCivil, Etnia, TipoDiscapacidad, TipoSangre, Habitante, HabitanteDiscapacidad, HabitanteEstadoCivil, HabitanteEtnia, HabitanteNivelEstudio, HabitanteTipoSangre
from .serializers import NacionalidadSerializer, NivelEstudioSerializer, PaisOrigenSerializer, CelularSerializer, CorreoElectronicoSerializer, EstadoCivilSerializer, EtniaSerializer, TipoDiscapacidadSerializer, TipoSangreSerializer, HabitanteSerializer, HabitanteDiscapacidadSerializer, HabitanteEstadoCivilSerializer, HabitanteEtniaSerializer, HabitanteNivelEstudioSerializer, HabitanteTipoSangreSerializer

# Create your views here.

class NacionalidadViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer

class NivelEstudioViewSet(viewsets.ModelViewSet):
    queryset = NivelEstudio.objects.all()
    serializer_class = NivelEstudioSerializer

class PaisOrigenViewSet(viewsets.ModelViewSet):
    queryset = PaisOrigen.objects.all()
    serializer_class = PaisOrigenSerializer

class CelularViewSet(viewsets.ModelViewSet):
    queryset = Celular.objects.all()
    serializer_class = CelularSerializer

class CorreoElectronicoViewSet(viewsets.ModelViewSet):
    queryset = CorreoElectronico.objects.all()
    serializer_class = CorreoElectronicoSerializer

class EstadoCivilViewSet(viewsets.ModelViewSet):
    queryset = EstadoCivil.objects.all()
    serializer_class = EstadoCivilSerializer

class EtniaViewSet(viewsets.ModelViewSet):
    queryset = Etnia.objects.all()
    serializer_class = EtniaSerializer

class TipoDiscapacidadViewSet(viewsets.ModelViewSet):
    queryset = TipoDiscapacidad.objects.all()
    serializer_class = TipoDiscapacidadSerializer

class TipoSangreViewSet(viewsets.ModelViewSet):
    queryset = TipoSangre.objects.all()
    serializer_class = TipoSangreSerializer

class HabitanteViewSet(viewsets.ModelViewSet):
    queryset = Habitante.objects.all()
    serializer_class = HabitanteSerializer

class HabitanteDiscapacidadViewSet(viewsets.ModelViewSet):
    queryset = HabitanteDiscapacidad.objects.all()
    serializer_class = HabitanteDiscapacidadSerializer

class HabitanteEstadoCivilViewSet(viewsets.ModelViewSet):
    queryset = HabitanteEstadoCivil.objects.all()
    serializer_class = HabitanteEstadoCivilSerializer

class HabitanteEtniaViewSet(viewsets.ModelViewSet):
    queryset = HabitanteEtnia.objects.all()
    serializer_class = HabitanteEtniaSerializer

class HabitanteNivelEstudioViewSet(viewsets.ModelViewSet):
    queryset = HabitanteNivelEstudio.objects.all()
    serializer_class = HabitanteNivelEstudioSerializer

class HabitanteTipoSangreViewSet(viewsets.ModelViewSet):
    queryset = HabitanteTipoSangre.objects.all()
    serializer_class = HabitanteTipoSangreSerializer
