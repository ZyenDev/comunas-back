"""
URL configuration for comunas_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="API Comunas",
      default_version='v1',
      description="Documentación de la API de Comunas",
      terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@comunas.local"),
    #   license=openapi.License(name="BSD License"),
   ),
   public=True,
#    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/comunidades/', include('apps.DatosComunidad.urls')),
    path('api/habitantes/', include('apps.DatosHabitante.urls')),
    path('api/ubicaciones/', include('apps.DatosUbicacion.urls')),
    path('api/viviendas/', include('apps.DatosVivienda.urls')),
    path('api/login', views.login),
    path('api/logout', views.logout),
    path('api/register/admin', views.register_admin),
    path('api/register/parlamentario', views.admin_register_parlamentario),
    path('api/register/vocero', views.parlamentario_register_vocero),
    path('api/register/habitante', views.vocero_register_habitante),
    path('api/toggle_user', views.toggle_user_status),
    path('api/groups/<str:group_name>/users/', views.get_users_by_group),
    path('api/profile', views.profile),
    path('api/dashboard', views.Dashboard),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
