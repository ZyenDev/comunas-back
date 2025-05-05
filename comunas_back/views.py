from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from .serializers import UserSerializer
from .permissions import IsParlamentario, IsVocero, IsAdminOrParlamentarioOrVocero, IsAdminOrParlamentarioOrVoceroOrHabitante
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from django.apps import apps


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
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def register_admin(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(email=serializer.data['email'])
        user.set_password(serializer.data['password'])
        user.is_staff = True  # Para dar acceso a endpoints con IsAdminUser
        user.is_superuser = True  # Para permisos totales
        user.save()

        # Asignar el grupo "Administrador" directamente
        group_name = "Administrador"  # Nombre del grupo que deseas asignar
        group, created = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)

        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def admin_register_parlamentario(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(email=serializer.data['email'])
        user.set_password(serializer.data['password'])
        user.save()

      # Asignar el grupo "Parlamentario" directamente
        group_name = "Parlamentario"  # Nombre del grupo que deseas asignar
        group, created = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)

        return Response({"message": "Usuario creado exitosamente", "user": serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsParlamentario])
def parlamentario_register_vocero(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(email=serializer.data['email'])
        user.set_password(serializer.data['password'])
        user.save()

        group_name = "Vocero"  # Nombre del grupo que deseas asignar
        group, created = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)

        return Response({"message": "Usuario creado exitosamente", "user": serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsVocero])
def vocero_register_habitante(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(email=serializer.data['email'])
        user.set_password(serializer.data['password'])
        user.save()

        group_name = "Habitante"
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


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminOrParlamentarioOrVocero])
def toggle_user_status(request):
    """
    Habilita o deshabilita un usuario cambiando el estado de is_active.
    """
    user_id = request.data.get("user_id")
    is_active = request.data.get("is_active")

    if user_id is None or is_active is None:
        return Response({"error": "Se requieren los campos 'user_id' y 'is_active'."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(id=user_id)
        user.is_active = is_active  # Cambia el estado de is_active
        user.save()
        status_message = "habilitado" if is_active else "deshabilitado"
        return Response({"message": f"El usuario {user.username} ha sido {status_message} exitosamente."}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminOrParlamentarioOrVocero])
def get_users_by_group(request, group_name):
    try:
        group = Group.objects.get(name=group_name)  # Busca el grupo por nombre
        users = group.user_set.all()  # Obtiene todos los usuarios asociados al grupo
        serializer = UserSerializer(users, many=True)  # Serializa los usuarios
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Group.DoesNotExist:
        return Response({"error": f"El grupo '{group_name}' no existe."}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminOrParlamentarioOrVocero])
def get_users_by_group(request, group_name):
    try:
        group = Group.objects.get(name=group_name)  # Busca el grupo por nombre
        users = group.user_set.all()  # Obtiene todos los usuarios asociados al grupo
        serializer = UserSerializer(users, many=True)  # Serializa los usuarios
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Group.DoesNotExist:
        return Response({"error": f"El grupo '{group_name}' no existe."}, status=status.HTTP_404_NOT_FOUND)
