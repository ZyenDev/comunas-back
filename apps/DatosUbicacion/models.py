from django.db import models


class AmbitoTerritorial(models.Model):
    id_ambito_territorial = models.AutoField(primary_key=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    latitud = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'ambito_territorial'
        ordering = ['id_ambito_territorial']


class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'estado'


class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_estado = models.ForeignKey(
        Estado, models.DO_NOTHING, db_column='id_estado')

    class Meta:
        managed = False
        db_table = 'municipio'


class Parroquia(models.Model):
    id_parroquia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_municipio = models.ForeignKey(
        Municipio, models.DO_NOTHING, db_column='id_municipio')

    class Meta:
        managed = False
        db_table = 'parroquia'


class Sector(models.Model):
    id_sector = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_parroquia = models.ForeignKey(
        Parroquia, models.DO_NOTHING, db_column='id_parroquia')

    class Meta:
        managed = False
        db_table = 'sector'


class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=100)
    id_sector = models.ForeignKey(
        Sector, models.DO_NOTHING, db_column='id_sector')
    id_parroquia = models.ForeignKey(
        Parroquia, models.DO_NOTHING, db_column='id_parroquia')

    class Meta:
        managed = False
        db_table = 'ubicacion'
        ordering = ['id_ubicacion']
