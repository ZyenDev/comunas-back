from django.db import models
from apps.DatosVivienda.models import Vivienda

class Nacionalidad(models.Model):
    id_nacionalidad = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=12)

    class Meta:
        managed = False
        db_table = 'nacionalidad'

class NivelEstudio(models.Model):
    id_nivel_estudio = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'nivel_estudio'

class PaisOrigen(models.Model):
    id_pais_origen = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'pais_origen'

class Celular(models.Model):
    id_celular = models.AutoField(primary_key=True)
    codigo_operadora = models.CharField(max_length=5)
    numero = models.CharField(max_length=15)
    id_habitante = models.ForeignKey('Habitante', models.DO_NOTHING, db_column='id_habitante')

    class Meta:
        managed = False
        db_table = 'celular'
        unique_together = (('codigo_operadora', 'numero'),)

class CorreoElectronico(models.Model):
    id_correo = models.AutoField(primary_key=True)
    correo = models.CharField(unique=True, max_length=100)
    id_habitante = models.ForeignKey('Habitante', models.DO_NOTHING, db_column='id_habitante')

    class Meta:
        managed = False
        db_table = 'correo_electronico'

class EstadoCivil(models.Model):
    id_estado_civil = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_civil'

class Etnia(models.Model):
    id_etnia = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'etnia'

class TipoDiscapacidad(models.Model):
    id_tipo_discapacidad = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_discapacidad'

class TipoSangre(models.Model):
    id_tipo_sangre = models.AutoField(primary_key=True)
    tipo = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_sangre'

class Habitante(models.Model):
    id_habitante = models.AutoField(primary_key=True)
    cedula = models.CharField(unique=True, max_length=20)
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100, blank=True, null=True)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    sexo = models.CharField(max_length=9)
    discapacidad = models.BooleanField()
    id_nacionalidad = models.ForeignKey('Nacionalidad', models.DO_NOTHING, db_column='id_nacionalidad')
    id_pais_origen = models.ForeignKey('PaisOrigen', models.DO_NOTHING, db_column='id_pais_origen', blank=True, null=True)
    id_vivienda = models.ForeignKey(Vivienda, models.DO_NOTHING, db_column='id_vivienda')
    pertenece_etnia = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'habitante'

class HabitanteDiscapacidad(models.Model):
    id_habitante = models.OneToOneField(Habitante, models.DO_NOTHING, db_column='id_habitante', primary_key=True)  # The composite primary key (id_habitante, id_tipo_discapacidad) found, that is not supported. The first column is selected.
    id_tipo_discapacidad = models.ForeignKey('TipoDiscapacidad', models.DO_NOTHING, db_column='id_tipo_discapacidad')

    class Meta:
        managed = False
        db_table = 'habitante_discapacidad'
        unique_together = (('id_habitante', 'id_tipo_discapacidad'),)

class HabitanteEstadoCivil(models.Model):
    id_habitante = models.OneToOneField(Habitante, models.DO_NOTHING, db_column='id_habitante', primary_key=True)  # The composite primary key (id_habitante, id_estado_civil) found, that is not supported. The first column is selected.
    id_estado_civil = models.ForeignKey(EstadoCivil, models.DO_NOTHING, db_column='id_estado_civil')

    class Meta:
        managed = False
        db_table = 'habitante_estado_civil'
        unique_together = (('id_habitante', 'id_estado_civil'),)

class HabitanteEtnia(models.Model):
    id_habitante = models.OneToOneField(Habitante, models.DO_NOTHING, db_column='id_habitante', primary_key=True)  # The composite primary key (id_habitante, id_etnia) found, that is not supported. The first column is selected.
    id_etnia = models.ForeignKey(Etnia, models.DO_NOTHING, db_column='id_etnia')

    class Meta:
        managed = False
        db_table = 'habitante_etnia'
        unique_together = (('id_habitante', 'id_etnia'),)

class HabitanteNivelEstudio(models.Model):
    id_habitante = models.OneToOneField(Habitante, models.DO_NOTHING, db_column='id_habitante', primary_key=True)  # The composite primary key (id_habitante, id_nivel_estudio) found, that is not supported. The first column is selected.
    id_nivel_estudio = models.ForeignKey('NivelEstudio', models.DO_NOTHING, db_column='id_nivel_estudio')

    class Meta:
        managed = False
        db_table = 'habitante_nivel_estudio'
        unique_together = (('id_habitante', 'id_nivel_estudio'),)

class HabitanteTipoSangre(models.Model):
    id_habitante = models.OneToOneField(Habitante, models.DO_NOTHING, db_column='id_habitante', primary_key=True)  # The composite primary key (id_habitante, id_tipo_sangre) found, that is not supported. The first column is selected.
    id_tipo_sangre = models.ForeignKey('TipoSangre', models.DO_NOTHING, db_column='id_tipo_sangre')

    class Meta:
        managed = False
        db_table = 'habitante_tipo_sangre'
        unique_together = (('id_habitante', 'id_tipo_sangre'),)

