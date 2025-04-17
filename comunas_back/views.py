from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from .serializers import UserSerializer
from .permissions import IsParlamentario, IsVocero
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404

@api_view(["POST"])
def login(request):
    
    user = get_object_or_404(User, email=request.data["email"])

    if not user.check_password(request.data['password']):
        return Response({"error": "¡Contraseña invalida!"}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({"token": token.key, "email": serializer.data}, status=status.HTTP_200_OK)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response(status=status.HTTP_200_OK)
    except Token.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def register_admin(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(email=serializer.data['email'])
        user.set_password(serializer.data['password'])
        user.is_staff = True  # Para dar acceso a endpoints con IsAdminUser
        user.is_superuser = True  # Para permisos totales
        user.save()

        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])  # Solo administradores pueden acceder
def admin_register_parlamentario(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(email=serializer.data['email'])
        user.set_password(serializer.data['password'])
        user.save()

        # Asignar grupo al usuario si se envía en la solicitud
        group_name = request.data.get('Parlamentario')
        if group_name:
            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)

        return Response({"message": "Usuario creado exitosamente", "user": serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsParlamentario])  # Solo administradores pueden acceder
def parlamentario_register_vocero(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(email=serializer.data['email'])
        user.set_password(serializer.data['password'])
        user.save()

        # Asignar grupo al usuario si se envía en la solicitud
        group_name = request.data.get('Vocero')
        if group_name:
            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)

        return Response({"message": "Usuario creado exitosamente", "user": serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsVocero])  # Solo administradores pueden acceder
def vocero_register_habitante(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(email=serializer.data['email'])
        user.set_password(serializer.data['password'])
        user.save()

        # Asignar grupo al usuario si se envía en la solicitud
        group_name = request.data.get('Habitante')
        if group_name:
            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)

        return Response({"message": "Usuario creado exitosamente", "user": serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):

    # Logica de Profile
    print(request.user)
    serializer = UserSerializer(instance=request.user)

    # return Response("Estas en la sesion de {}".format(request.user.user.username), status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_200_OK)