from rest_framework.permissions import BasePermission


class IsParlamentario(BasePermission):
    def has_permission(self, request, view):
        # Verifica si el usuario pertenece al grupo 'Parlamentario'
        return request.user.groups.filter(name='Parlamentario').exists()


class IsVocero(BasePermission):
    def has_permission(self, request, view):
        # Verifica si el usuario pertenece al grupo 'Parlamentario'
        return request.user.groups.filter(name='Vocero').exists()


class IsAdminOrParlamentarioOrVocero(BasePermission):
    """
    Permite el acceso si el usuario es administrador, parlamentario o vocero.
    """

    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated and (
                request.user.is_staff or  # Admin
                # Parlamentario
                request.user.groups.filter(name="Parlamentario").exists() or
                request.user.groups.filter(name="Vocero").exists()  # Vocero
            )
        )
