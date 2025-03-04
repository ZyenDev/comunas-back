from rest_framework import serializers
from .models import Comuna, ConsejoComunal

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'

class ConsejoComunalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsejoComunal
        fields = '__all__'
    