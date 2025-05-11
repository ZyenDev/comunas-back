from rest_framework import serializers
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField()  # Campo para asignar grupo
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'group', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True}  # ¡Esto evita que se devuelva el password!
        }
    
    def get_group(self, obj):
        # Obtiene el primer grupo del usuario, si existe
        groups = obj.groups.values_list('name', flat=True)
        return groups[0] if groups else None