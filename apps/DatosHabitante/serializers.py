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


class HabitanteSerializer(serializers.ModelSerializer):
    celular = CelularSerializer(source='celular_set', many=True, read_only=True)
    tipo_sangre = serializers.SerializerMethodField()

    class Meta:
        model = Habitante
        fields = '__all__'

    def get_tipo_sangre(self, obj):
        # Manejo robusto para evitar errores si no hay relación o datos
        try:
            rel = getattr(obj, 'habitantetiposangre_set', None)
            if rel:
                rel = rel.select_related('id_tipo_sangre').first()
                if rel and rel.id_tipo_sangre:
                    return rel.id_tipo_sangre.tipo
        except Exception:
            pass
        return None
    

class HabitanteDiscapacidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitanteDiscapacidad
        fields = '__all__'


class HabitanteEstadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitanteEstadoCivil
        fields = '__all__'


class HabitanteEtniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitanteEtnia
        fields = '__all__'


class HabitanteNivelEstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitanteNivelEstudio
        fields = '__all__'


class HabitanteTipoSangreSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitanteTipoSangre
        fields = '__all__'
