from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'comunas', views.ComunaViewSet)
router.register(r'consejoscomunales', views.ConsejoComunalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
