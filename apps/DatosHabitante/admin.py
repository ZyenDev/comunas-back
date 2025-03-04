from django.contrib import admin
from .models import  Nacionalidad, NivelEstudio, PaisOrigen, Celular, CorreoElectronico, EstadoCivil, Etnia, TipoDiscapacidad, TipoSangre, Habitante, HabitanteDiscapacidad, HabitanteEstadoCivil, HabitanteEtnia, HabitanteNivelEstudio, HabitanteTipoSangre

# Register your models here.

admin.site.register(Nacionalidad)
admin.site.register(NivelEstudio)
admin.site.register(PaisOrigen)
admin.site.register(Celular)
admin.site.register(CorreoElectronico)
admin.site.register(EstadoCivil)
admin.site.register(Etnia)
admin.site.register(TipoDiscapacidad)
admin.site.register(TipoSangre)
admin.site.register(Habitante)
admin.site.register(HabitanteDiscapacidad)
admin.site.register(HabitanteEstadoCivil)
admin.site.register(HabitanteEtnia)
admin.site.register(HabitanteNivelEstudio)
admin.site.register(HabitanteTipoSangre)