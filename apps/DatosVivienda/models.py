from django.db import models
from apps.DatosUbicacion.models import Ubicacion
from apps.DatosComunidad.models import ConsejoComunal

class ServiciosBasicos(models.Model):
    id_servicios = models.AutoField(primary_key=True)
    agua = models.BooleanField()
    electricidad = models.BooleanField()
    gas = models.BooleanField()
    internet = models.BooleanField()
    aseo = models.BooleanField()
    cloaca = models.BooleanField()
    id_vivienda = models.ForeignKey('Vivienda', models.DO_NOTHING, db_column='id_vivienda')

    class Meta:
        managed = False
        db_table = 'servicios_basicos'

class SituacionVivienda(models.Model):
    id_situacion_vivienda = models.AutoField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'situacion_vivienda'

class Telefono(models.Model):
    id_telefono = models.AutoField(primary_key=True)
    codigo_area = models.CharField(max_length=5)
    numero = models.CharField(max_length=15)
    id_vivienda = models.ForeignKey('Vivienda', models.DO_NOTHING, db_column='id_vivienda')

    class Meta:
        managed = False
        db_table = 'telefono'
        unique_together = (('codigo_area', 'numero'),)

class TipoOcupacionVivienda(models.Model):
    id_tipo_ocupacion = models.AutoField(primary_key=True)
    vivienda_ocupada = models.BooleanField()
    subtipo_ocupacion = models.CharField(max_length=35)
    tiene_documentacion = models.BooleanField()
    respuesta_otro = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_ocupacion_vivienda'

class TipoPared(models.Model):
    id_tipo_pared = models.AutoField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_pared'

class TipoPiso(models.Model):
    id_tipo_piso = models.AutoField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_piso'

class TipoTecho(models.Model):
    id_tipo_techo = models.AutoField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_techo'

class TipoVivienda(models.Model):
    id_tipo_vivienda = models.AutoField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_vivienda'

class Vivienda(models.Model):
    id_vivienda = models.AutoField(primary_key=True)
    id_ubicacion = models.ForeignKey(Ubicacion, models.DO_NOTHING, db_column='id_ubicacion')
    numero_vivienda = models.CharField(max_length=20)
    cantidad_habitantes = models.IntegerField()
    cantidad_familias = models.IntegerField()
    cantidad_banos = models.IntegerField()
    cantidad_cuartos = models.IntegerField()
    id_consejo_comunal = models.ForeignKey(ConsejoComunal, models.DO_NOTHING, db_column='id_consejo_comunal')
    id_tipo_vivienda = models.ForeignKey(TipoVivienda, models.DO_NOTHING, db_column='id_tipo_vivienda')
    id_tipo_techo = models.ForeignKey(TipoTecho, models.DO_NOTHING, db_column='id_tipo_techo')
    id_tipo_pared = models.ForeignKey(TipoPared, models.DO_NOTHING, db_column='id_tipo_pared')
    id_tipo_piso = models.ForeignKey(TipoPiso, models.DO_NOTHING, db_column='id_tipo_piso')
    id_situacion_vivienda = models.ForeignKey(SituacionVivienda, models.DO_NOTHING, db_column='id_situacion_vivienda')
    id_tipo_ocupacion_vivienda = models.ForeignKey(TipoOcupacionVivienda, models.DO_NOTHING, db_column='id_tipo_ocupacion_vivienda')

    class Meta:
        managed = False
        db_table = 'vivienda'
