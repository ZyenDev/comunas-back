from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet


# Solo usuarios autenticados pueden acceder
@permission_classes([IsAuthenticated])
class ReporteVoceroParlamentario(ViewSet):
    """
    ViewSet para generar reportes de parlamentarios, sin necesidad de consejo comunal asignado.
    """

    def create(self, request):
        tipo_reporte = request.data.get("tipo_reporte")
        genero = request.data.get("genero")  # 'M' o 'F' o None
        consejo_comunal_id = request.data.get("consejo_comunal_id")  # ID del consejo comunal

        Habitante = apps.get_model('DatosHabitante', 'Habitante')
        Discapacidad = apps.get_model('DatosHabitante', 'HabitanteDiscapacidad')
        Vivienda = apps.get_model('DatosVivienda', 'Vivienda')

        # Reporte: Todos los habitantes que pertenecen a una etnia
        if tipo_reporte == "habitantes_etnia":
            qs = Habitante.objects.exclude(id_etnia=None)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values("id_habitante", "nombre", "apellido", "sexo", "id_etnia__nombre"))
            return Response({"tipo_reporte": "habitantes_etnia", "data": data}, status=200)

        # Reporte: Todos los habitantes con discapacidad
        elif tipo_reporte == "habitantes_discapacidad":
            qs = Habitante.objects.filter(discapacidad=True)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values("id_habitante", "nombre", "apellido", "sexo"))
            return Response({"tipo_reporte": "habitantes_discapacidad", "data": data}, status=200)

        # Reporte: Todos los habitantes con discapacidad específica
        elif tipo_reporte == "habitantes_discapacidad_especifica":
            discapacidad_nombre = request.data.get("discapacidad")
            qs = Habitante.objects.filter(discapacidad=True, habitantediscapacidad__id_tipo_discapacidad__nombre=discapacidad_nombre)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values("id_habitante", "nombre", "apellido", "sexo", "habitantediscapacidad__id_tipo_discapacidad__nombre"))
            return Response({"tipo_reporte": "habitantes_discapacidad_especifica", "data": data}, status=200)

        # Reporte: Todos los habitantes de la tercera edad
        elif tipo_reporte == "habitantes_tercera_edad":
            qs = Habitante.objects.filter(edad__gte=60)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values("id_habitante", "nombre", "apellido", "sexo", "edad"))
            return Response({"tipo_reporte": "habitantes_tercera_edad", "data": data}, status=200)

        # Reporte: Todos los habitantes que son jefe de casa
        elif tipo_reporte == "habitantes_jefe_casa":
            qs = Habitante.objects.filter(jefe_casa=True)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values("id_habitante", "nombre", "apellido", "sexo"))
            return Response({"tipo_reporte": "habitantes_jefe_casa", "data": data}, status=200)

        # Reporte: Todos los habitantes menores de edad
        elif tipo_reporte == "habitantes_menores_edad":
            qs = Habitante.objects.filter(edad__lt=18)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values("id_habitante", "nombre", "apellido", "sexo", "edad"))
            return Response({"tipo_reporte": "habitantes_menores_edad", "data": data}, status=200)

        # Reporte: Todos los habitantes y su grado de instrucción
        elif tipo_reporte == "habitantes_grado_instruccion":
            qs = Habitante.objects.exclude(id_grado_instruccion=None)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values("id_habitante", "nombre", "apellido", "sexo", "id_grado_instruccion__nombre"))
            return Response({"tipo_reporte": "habitantes_grado_instruccion", "data": data}, status=200)

        # Reporte: Todas las viviendas con "x cantidad de habitantes"
        elif tipo_reporte == "viviendas_cantidad_habitantes":
            cantidad = request.data.get("cantidad")
            qs = Vivienda.objects.filter(cantidad_habitantes=cantidad)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values())
            return Response({"tipo_reporte": "viviendas_cantidad_habitantes", "data": data}, status=200)

        # Reporte: Todas las viviendas de un tipo específico
        elif tipo_reporte == "viviendas_tipo":
            tipo = request.data.get("tipo")
            qs = Vivienda.objects.filter(id_tipo_vivienda__nombre=tipo)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values())
            return Response({"tipo_reporte": "viviendas_tipo", "data": data}, status=200)

        # Reporte: Todas las viviendas con "x cantidad de familias"
        elif tipo_reporte == "viviendas_cantidad_familias":
            cantidad = request.data.get("cantidad")
            qs = Vivienda.objects.filter(cantidad_familias=cantidad)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values())
            return Response({"tipo_reporte": "viviendas_cantidad_familias", "data": data}, status=200)

        # Reporte: Todas las viviendas con "todos los tipos de techo"
        elif tipo_reporte == "viviendas_tipo_techo":
            tipo = request.data.get("tipo_techo")
            qs = Vivienda.objects.filter(id_tipo_techo__nombre=tipo)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values())
            return Response({"tipo_reporte": "viviendas_tipo_techo", "data": data}, status=200)

        # Reporte: Todas las viviendas con "todos los tipos de pared"
        elif tipo_reporte == "viviendas_tipo_pared":
            tipo = request.data.get("tipo_pared")
            qs = Vivienda.objects.filter(id_tipo_pared__nombre=tipo)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values())
            return Response({"tipo_reporte": "viviendas_tipo_pared", "data": data}, status=200)

        # Reporte: Todas las viviendas con "todas las situaciones de la vivienda"
        elif tipo_reporte == "viviendas_situacion":
            situacion = request.data.get("situacion")
            qs = Vivienda.objects.filter(id_situacion_vivienda__nombre=situacion)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values())
            return Response({"tipo_reporte": "viviendas_situacion", "data": data}, status=200)

        # Reporte: Todas las viviendas "ocupada / no ocupada"
        elif tipo_reporte == "viviendas_ocupacion":
            ocupada = request.data.get("ocupada")  # True/False
            nombre_ocupacion = "Ocupada" if ocupada else "No Ocupada"
            qs = Vivienda.objects.filter(id_tipo_ocupacion_vivienda__nombre=nombre_ocupacion)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values())
            return Response({"tipo_reporte": "viviendas_ocupacion", "data": data}, status=200)

        else:
            return Response({"error": "Tipo de reporte no válido."}, status=400)


# Esta vista devuelve la cantidad de registros de cada modelo en el proyecto.
@permission_classes([IsAuthenticated])
class DashboardViewSet(ViewSet):
    def list(self, request):
        Comunidad = apps.get_model('DatosComunidad', 'Comuna')
        Vivienda = apps.get_model('DatosVivienda', 'Vivienda')
        ConsejoComunal = apps.get_model('DatosComunidad', 'ConsejoComunal')

        numero_habitantes = User.objects.filter(
            groups__name="Habitante").count()
        numero_parlamentarios = User.objects.filter(
            groups__name="Parlamentario").count()
        numero_voceros = User.objects.filter(groups__name="Vocero").count()
        numero_administradores = User.objects.filter(is_staff=True).count()
        numero_viviendas = Vivienda.objects.count()
        numero_comunas = Comunidad.objects.count()
        numero_consejos_comunales = ConsejoComunal.objects.count()

        report = {
            "numero_habitantes": numero_habitantes,
            "numero_parlamentarios": numero_parlamentarios,
            "numero_voceros": numero_voceros,
            "numero_administradores": numero_administradores,
            "numero_viviendas": numero_viviendas,
            "numero_comunas": numero_comunas,
            "numero_consejos_comunales": numero_consejos_comunales,
        }

        return Response(report, status=200)
