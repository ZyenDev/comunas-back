from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet


# @permission_classes([IsAuthenticated])
# class ReporteAdministradorViewSet(ViewSet):
#     """
#     ViewSet para generar reportes de administrador.
#     """

#     def create(self, request):
#         """
#         Genera reportes según los parámetros enviados en la solicitud.
#         """
#         # Obtener parámetros de la solicitud
#         consejo_comunal_id = request.query_params.get(
#             "consejo_comunal_id")  # ID del consejo comunal
#         tipo_reporte = request.query_params.get(
#             "tipo_reporte")  # Tipo de reporte solicitado
#         rango_edad_min = request.query_params.get(
#             "edad_min")  # Edad mínima (opcional)
#         rango_edad_max = request.query_params.get(
#             "edad_max")  # Edad máxima (opcional)

#         # Obtener modelos
#         Comunidad = apps.get_model('DatosComunidad', 'Comuna')
#         Vivienda = apps.get_model('DatosVivienda', 'Vivienda')
#         ConsejoComunal = apps.get_model('DatosComunidad', 'ConsejoComunal')
#         Habitante = apps.get_model('DatosHabitante', 'Habitante')

#         # Filtrar por consejo comunal si se proporciona
#         consejo_comunal = None
#         if consejo_comunal_id:
#             consejo_comunal = ConsejoComunal.objects.filter(
#                 id=consejo_comunal_id).first()
#             if not consejo_comunal:
#                 return Response({"error": "Consejo comunal no encontrado."}, status=404)

#         # Generar el reporte según el tipo solicitado
#         if tipo_reporte == "habitantes":
#             habitantes = Habitante.objects.all()
#             if consejo_comunal:
#                 habitantes = habitantes.filter(consejo_comunal=consejo_comunal)

#             # Aplicar filtros adicionales
#             if rango_edad_min:
#                 habitantes = habitantes.filter(edad__gte=int(rango_edad_min))
#             if rango_edad_max:
#                 habitantes = habitantes.filter(edad__lte=int(rango_edad_max))

#             data = [{"id": h.id, "nombre": h.nombre, "edad": h.edad}
#                     for h in habitantes]
#             return Response({"tipo_reporte": "habitantes", "data": data}, status=200)

#         elif tipo_reporte == "viviendas":
#             viviendas = Vivienda.objects.all()
#             if consejo_comunal:
#                 viviendas = viviendas.filter(consejo_comunal=consejo_comunal)

#             data = [{"id": v.id, "direccion": v.direccion,
#                      "estado": v.estado} for v in viviendas]
#             return Response({"tipo_reporte": "viviendas", "data": data}, status=200)

#         elif tipo_reporte == "comuna":
#             comunas = Comunidad.objects.all()
#             data = [{"id": c.id, "nombre": c.nombre,
#                      "descripcion": c.descripcion} for c in comunas]
#             return Response({"tipo_reporte": "comuna", "data": data}, status=200)

#         else:
#             return Response({"error": "Tipo de reporte no válido."}, status=400)


# Solo usuarios autenticados pueden acceder
@permission_classes([IsAuthenticated])
class ReporteBasicoViewSet(ViewSet):
    """
    ViewSet para generar reportes de parlamentarios, sin necesidad de consejo comunal asignado.
    """

    def create(self, request):
        """
        Genera reportes según los parámetros enviados en la solicitud.
        """
        # Obtener modelos
        Vivienda = apps.get_model('DatosVivienda', 'Vivienda')
        ServiciosBasicos = apps.get_model('DatosVivienda', 'ServiciosBasicos')
        HabitanteDiscapacidad = apps.get_model('DatosHabitante', 'HabitanteDiscapacidad')
        Habitante = apps.get_model('DatosHabitante', 'Habitante')

        # Obtener parámetros de la solicitud
        tipo_reporte = request.data.get("tipo_reporte")  # Tipo de reporte solicitado

        # Generar el reporte según el tipo solicitado
        if tipo_reporte == "habitantes":
            habitantes = Habitante.objects.all()
            data = list(habitantes.values())
            return Response({"tipo_reporte": "habitantes", "data": data}, status=200)

        elif tipo_reporte == "viviendas":
            viviendas = Vivienda.objects.prefetch_related('servicios_basicos').all()
        
            data = []
            for vivienda in viviendas:
                # Obtener los servicios básicos relacionados con la vivienda
                servicios_basicos = vivienda.servicios_basicos.values(
                    'id_servicios', 'agua', 'electricidad', 'gas', 'internet', 'aseo', 'cloaca'
                ).first()  # Obtener el primer registro de servicios básicos (si existe)
        
                # Construir la respuesta para cada vivienda
                data.append({
                    "id_vivienda": vivienda.id_vivienda,
                    "numero_vivienda": vivienda.numero_vivienda,
                    "cantidad_habitantes": vivienda.cantidad_habitantes,
                    "cantidad_familias": vivienda.cantidad_familias,
                    "cantidad_banos": vivienda.cantidad_banos,
                    "cantidad_cuartos": vivienda.cantidad_cuartos,
                    "id_ubicacion": vivienda.id_ubicacion.id if vivienda.id_ubicacion else None,
                    "id_consejo_comunal": vivienda.id_consejo_comunal.id if vivienda.id_consejo_comunal else None,
                    "id_tipo_vivienda": vivienda.id_tipo_vivienda.id if vivienda.id_tipo_vivienda else None,
                    "id_tipo_techo": vivienda.id_tipo_techo.id if vivienda.id_tipo_techo else None,
                    "id_tipo_pared": vivienda.id_tipo_pared.id if vivienda.id_tipo_pared else None,
                    "id_tipo_piso": vivienda.id_tipo_piso.id if vivienda.id_tipo_piso else None,
                    "id_situacion_vivienda": vivienda.id_situacion_vivienda.id if vivienda.id_situacion_vivienda else None,
                    "id_tipo_ocupacion_vivienda": vivienda.id_tipo_ocupacion_vivienda.id if vivienda.id_tipo_ocupacion_vivienda else None,
                    "servicios_basicos": servicios_basicos if servicios_basicos else {
                        "id_servicios": None,
                        "agua": None,
                        "electricidad": None,
                        "gas": None,
                        "internet": None,
                        "aseo": None,
                        "cloaca": None
                    }
                })
        
            return Response({"tipo_reporte": "viviendas", "data": data}, status=200)

        elif tipo_reporte == "habitantes_discapacitados":
            # Filtrar habitantes que tienen discapacidad
            habitantes_discapacitados = Habitante.objects.filter(discapacidad=True)

            data = []
            for habitante in habitantes_discapacitados:
                # Obtener las discapacidades relacionadas con el habitante
                discapacidades = HabitanteDiscapacidad.objects.filter(id_habitante=habitante.id_habitante).select_related('id_tipo_discapacidad').values(
                    'id_tipo_discapacidad__nombre', 'id_tipo_discapacidad__descripcion'
                )

                # Construir la respuesta para cada habitante
                data.append({
                    "id": habitante.id_habitante,
                    "nombre": habitante.primer_nombre,
                    "apellido": habitante.primer_apellido,
                    "edad": habitante.edad,
                    "discapacidades": list(discapacidades)
                })

            return Response({"tipo_reporte": "habitantes_discapacitados", "data": data}, status=200)

        else:
            return Response({"error": "Tipo de reporte no válido."}, status=400)
        
# # Solo usuarios autenticados pueden acceder
# @permission_classes([IsAuthenticated])
# class ReporteVoceroViewSet(ViewSet):
#     """
#     ViewSet para generar reportes de voceros, limitado a su consejo comunal asignado.
#     """

#     def list(self, request):
#         """
#         Genera reportes según los parámetros enviados en la solicitud.
#         """
#         # Obtener modelos
#         ConsejoComunal = apps.get_model('DatosComunidad', 'ConsejoComunal')
#         Vivienda = apps.get_model('DatosVivienda', 'Vivienda')
#         Habitante = apps.get_model('DatosHabitante', 'Habitante')

#         # Suponiendo que el usuario tiene un campo relacionado con su consejo comunal
#         usuario = request.user
#         # Ajusta según tu modelo
#         consejo_comunal = getattr(usuario, 'consejo_comunal', None)

#         if not consejo_comunal:
#             return Response({"error": "No tienes un consejo comunal asignado."}, status=403)

#         # Obtener parámetros de la solicitud
#         tipo_reporte = request.query_params.get(
#             "tipo_reporte")  # Tipo de reporte solicitado
#         rango_edad_min = request.query_params.get(
#             "edad_min")  # Edad mínima (opcional)
#         rango_edad_max = request.query_params.get(
#             "edad_max")  # Edad máxima (opcional)
#         # Cantidad de personas en viviendas (opcional)
#         cantidad_personas = request.query_params.get("cantidad_personas")
#         # Cantidad de familias en viviendas (opcional)
#         cantidad_familias = request.query_params.get("cantidad_familias")

#         # Generar el reporte según el tipo solicitado
#         if tipo_reporte == "habitantes":
#             habitantes = Habitante.objects.filter(
#                 consejo_comunal=consejo_comunal)

#             # Aplicar filtros adicionales
#             if rango_edad_min:
#                 habitantes = habitantes.filter(edad__gte=int(rango_edad_min))
#             if rango_edad_max:
#                 habitantes = habitantes.filter(edad__lte=int(rango_edad_max))

#             data = [{"id": h.id, "nombre": h.nombre, "edad": h.edad}
#                     for h in habitantes]
#             return Response({"tipo_reporte": "habitantes", "data": data}, status=200)

#         elif tipo_reporte == "habitantes_discapacitados":
#             habitantes_discapacitados = Habitante.objects.filter(
#                 consejo_comunal=consejo_comunal, discapacidad__isnull=False
#             )
#             data = [{"id": h.id, "nombre": h.nombre, "discapacidad": h.discapacidad}
#                     for h in habitantes_discapacitados]
#             return Response({"tipo_reporte": "habitantes_discapacitados", "data": data}, status=200)

#         elif tipo_reporte == "viviendas":
#             viviendas = Vivienda.objects.filter(
#                 consejo_comunal=consejo_comunal)

#             # Aplicar filtros adicionales
#             if cantidad_personas:
#                 viviendas = viviendas.filter(
#                     cantidad_personas__gte=int(cantidad_personas))
#             if cantidad_familias:
#                 viviendas = viviendas.filter(
#                     cantidad_familias__gte=int(cantidad_familias))

#             data = [{"id": v.id, "direccion": v.direccion,
#                      "estado": v.estado} for v in viviendas]
#             return Response({"tipo_reporte": "viviendas", "data": data}, status=200)

#         elif tipo_reporte == "viviendas_construccion":
#             viviendas_construccion = Vivienda.objects.filter(
#                 consejo_comunal=consejo_comunal, estado="En construcción")
#             data = [{"id": v.id, "direccion": v.direccion}
#                     for v in viviendas_construccion]
#             return Response({"tipo_reporte": "viviendas_construccion", "data": data}, status=200)

#         elif tipo_reporte == "viviendas_abandono":
#             viviendas_abandono = Vivienda.objects.filter(
#                 consejo_comunal=consejo_comunal, estado="Abandono")
#             data = [{"id": v.id, "direccion": v.direccion}
#                     for v in viviendas_abandono]
#             return Response({"tipo_reporte": "viviendas_abandono", "data": data}, status=200)

#         else:
#             return Response({"error": "Tipo de reporte no válido."}, status=400)


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
