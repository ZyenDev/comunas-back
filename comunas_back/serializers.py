from rest_framework import serializers
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.ModelSerializer):
    group = serializers.CharField(write_only=True, required=False)  # Campo para asignar grupo
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'group']