from rest_framework import serializers
from .models import ServiciosBasicos, SituacionVivienda, Telefono, TipoOcupacionVivienda, TipoPared, TipoPiso, TipoTecho, TipoVivienda, Vivienda


class ServiciosBasicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiciosBasicos
        fields = '__all__'


class SituacionViviendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituacionVivienda
        fields = '__all__'


class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefono
        fields = '__all__'


class TipoOcupacionViviendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOcupacionVivienda
        fields = '__all__'


class TipoParedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPared
        fields = '__all__'


class TipoPisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPiso
        fields = '__all__'


class TipoTechoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTecho
        fields = '__all__'


class TipoViviendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVivienda
        fields = '__all__'


class ViviendaSerializer(serializers.ModelSerializer):
    servicios_basicos = ServiciosBasicosSerializer(many=True, read_only=True)

    class Meta:
        model = Vivienda
        fields = '__all__'
