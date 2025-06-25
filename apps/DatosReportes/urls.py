from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'general', views.DashboardViewSet,
                basename='dashboard')

router.register(r'administrador', views.ReporteAdministrador,
                basename='reporte-administrador')
router.register(r'parlamentario', views.ReporteParlamentario,
                basename='reporte-parlamentario')
router.register(r'vocero', views.ReporteVocero,
                basename='reporte-vocero')


urlpatterns = [
    path('', include(router.urls)),
    path('pdf/', views.HabitantePDFView.as_view(), name='constancia-pdf'),  # Agrega esta línea
]
