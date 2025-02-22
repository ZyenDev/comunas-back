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
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/comunidades/', include('apps.DatosComunidad.urls')),
    path('api/habitantes/', include('apps.DatosHabitante.urls')),
    path('api/ubicaciones/', include('apps.DatosUbicacion.urls')),
    path('api/viviendas/', include('apps.DatosVivienda.urls')),
    path('docs/', include_docs_urls(title='API Comunas')),
]
