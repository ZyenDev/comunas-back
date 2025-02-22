from django.contrib import admin
from .models import Vivienda, TipoVivienda, TipoOcupacionVivienda, TipoPared, TipoPiso, TipoTecho, SituacionVivienda, Telefono

# Register your models here.

admin.site.register(Vivienda)
admin.site.register(TipoVivienda)
admin.site.register(TipoOcupacionVivienda)
admin.site.register(TipoPared)
admin.site.register(TipoPiso)
admin.site.register(TipoTecho)
admin.site.register(SituacionVivienda)
admin.site.register(Telefono)