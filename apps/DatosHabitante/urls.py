from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'nacionalidad', views.NacionalidadViewSet)
router.register(r'nivelestudio', views.NivelEstudioViewSet)
router.register(r'paisorigen', views.PaisOrigenViewSet)
router.register(r'celular', views.CelularViewSet)
router.register(r'correoelectronico', views.CorreoElectronicoViewSet)
router.register(r'estadocivil', views.EstadoCivilViewSet)
router.register(r'etnia', views.EtniaViewSet)
router.register(r'tipodiscapacidad', views.TipoDiscapacidadViewSet)
router.register(r'tiposangre', views.TipoSangreViewSet)
router.register(r'habitante', views.HabitanteViewSet)
router.register(r'habitantediscapacidad', views.HabitanteDiscapacidadViewSet)
router.register(r'habitanteestadocivil', views.HabitanteEstadoCivilViewSet)
router.register(r'habitanteetnia', views.HabitanteEtniaViewSet)
router.register(r'habitantenivelestudio', views.HabitanteNivelEstudioViewSet)
router.register(r'habitantetiposangre', views.HabitanteTipoSangreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Ruta Habitante por Vivienda
    path('habitantes/vivienda/<int:id_vivienda>/', views.HabitantesPorViviendaView.as_view(), name='habitantes-por-vivienda'),
]
