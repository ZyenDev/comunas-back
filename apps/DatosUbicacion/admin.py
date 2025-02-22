from django.contrib import admin
from .models import Ubicacion, Sector, Parroquia, Municipio, Estado, AmbitoTerritorial

# Register your models here.

admin.site.register(Ubicacion)
admin.site.register(Sector)
admin.site.register(Parroquia)
admin.site.register(Municipio)
admin.site.register(Estado)
admin.site.register(AmbitoTerritorial)