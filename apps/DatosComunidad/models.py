from django.db import models
from apps.DatosUbicacion.models import AmbitoTerritorial

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    codigo_situr = models.CharField(unique=True, max_length=20)
    rif = models.CharField(unique=True, max_length=20)
    nombre = models.CharField(max_length=100)
    cantidad_consejo_comunal = models.IntegerField()
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)
    id_ambito_territorial = models.ForeignKey(AmbitoTerritorial, models.DO_NOTHING, db_column='id_ambito_territorial')

    class Meta:
        managed = False
        db_table = 'comuna'

class ConsejoComunal(models.Model):
    id_consejo_comunal = models.AutoField(primary_key=True)
    codigo_situr = models.CharField(unique=True, max_length=20)
    rif = models.CharField(unique=True, max_length=20)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)
    nombre = models.CharField(max_length=100)
    id_ambito_territorial = models.ForeignKey(AmbitoTerritorial, models.DO_NOTHING, db_column='id_ambito_territorial')
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')

    class Meta:
        managed = False
        db_table = 'consejo_comunal'
