from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'serviciosbasicos', views.ServiciosBasicosViewSet)
router.register(r'situacionvivienda', views.SituacionViviendaViewSet)
router.register(r'telefono', views.TelefonoViewSet)
router.register(r'tipoocupacionvivienda', views.TipoOcupacionViviendaViewSet)
router.register(r'tipopared', views.TipoParedViewSet)
router.register(r'tipopiso', views.TipoPisoViewSet)
router.register(r'tipotecho', views.TipoTechoViewSet)
router.register(r'tipovivienda', views.TipoViviendaViewSet)
router.register(r'vivienda', views.ViviendaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
