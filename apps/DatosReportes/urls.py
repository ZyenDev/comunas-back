from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'general', views.DashboardViewSet,
                basename='dashboard')
# router.register(r'administrador', views.ReporteAdministradorViewSet,
#                 basename='reporte-administrador')
router.register(r'parlamentario', views.ReporteVoceroParlamentario,
                basename='reporte-parlamentario')
# router.register(r'vocero', views.ReporteVoceroViewSet,
#                 basename='reporte-vocero')

urlpatterns = [
    path('', include(router.urls)),
]
