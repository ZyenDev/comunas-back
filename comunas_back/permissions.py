from rest_framework.permissions import BasePermission

class IsParlamentario(BasePermission):
    def has_permission(self, request, view):
        # Verifica si el usuario pertenece al grupo 'Parlamentario'
        return request.user.groups.filter(name='Parlamentario').exists()
    
class IsVocero(BasePermission):
    def has_permission(self, request, view):
        # Verifica si el usuario pertenece al grupo 'Parlamentario'
        return request.user.groups.filter(name='Vocero').exists()