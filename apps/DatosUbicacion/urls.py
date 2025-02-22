from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'ambitoterritorial', views.AmbitoTerritorialViewSet)
router.register(r'estado', views.EstadoViewSet)
router.register(r'municipio', views.MunicipioViewSet)
router.register(r'parroquia', views.ParroquiaViewSet)
router.register(r'sector', views.SectorViewSet)
router.register(r'ubicacion', views.UbicacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
