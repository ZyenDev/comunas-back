from rest_framework import serializers
from .models import Nacionalidad, NivelEstudio, PaisOrigen, Celular, CorreoElectronico, EstadoCivil, Etnia, TipoDiscapacidad, TipoSangre, Habitante, HabitanteDiscapacidad, HabitanteEstadoCivil, HabitanteEtnia, HabitanteNivelEstudio, HabitanteTipoSangre


class NacionalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nacionalidad
        fields = '__all__'


class NivelEstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelEstudio
        fields = '__all__'


class PaisOrigenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaisOrigen
        fields = '__all__'


class CelularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celular
        fields = '__all__'


class CorreoElectronicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorreoElectronico
        fields = '__all__'


class EstadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivil
        fields = '__all__'


class EtniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etnia
        fields = '__all__'


class TipoDiscapacidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDiscapacidad
        fields = '__all__'


class TipoSangreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSangre
        fields = '__all__'


class HabitanteEtniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitanteEtnia
        fields = '__all__'


class HabitanteSerializer(serializers.ModelSerializer):
    discapacidad = serializers.BooleanField(required=True)  # Booleano del modelo
    tipo_discapacidad = TipoDiscapacidadSerializer(
        source='habitantediscapacidad.id_tipo_discapacidad', read_only=True)  # Relación

    tipo_sangre = TipoSangreSerializer(
        source='habitantetiposangre.id_tipo_sangre', read_only=True)
    celular = CelularSerializer(
        source='celular_set', many=True, read_only=True)
    estado_civil =  EstadoCivilSerializer(
        source='habitanteestadocivil.id_estado_civil', read_only=True)
    nivel_estudio = NivelEstudioSerializer(
        source='habitantenivelestudio.id_nivel_estudio', read_only=True)
    etnia = EtniaSerializer(
        source='habitanteetnia.id_etnia', read_only=True)
    habitante_etnia = HabitanteEtniaSerializer(
        source='habitanteetnia', read_only=True)

    class Meta:
        model = Habitante
        fields = '__all__'  # O lista explícita de campos + 'tipo_discapacidad'


class HabitanteDiscapacidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitanteDiscapacidad
        fields = '__all__'


class HabitanteEstadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitanteEstadoCivil
        fields = '__all__'


class HabitanteNivelEstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitanteNivelEstudio
        fields = '__all__'


class HabitanteTipoSangreSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitanteTipoSangre
        fields = '__all__'
