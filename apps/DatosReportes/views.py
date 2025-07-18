from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework import status
from datetime import date, timedelta


# Solo usuarios autenticados pueden acceder
@permission_classes([IsAuthenticated])
class ReporteAdministrador(ViewSet):
    def create(self, request):
        tipo_reporte = request.data.get("tipo_reporte")
        genero = request.data.get("genero")  # 'M' o 'F' o None
        comuna_id = request.data.get("comuna_id")  # ID de la comuna

        ConsejoComunal = apps.get_model('DatosComunidad', 'ConsejoComunal')
        Habitante = apps.get_model('DatosHabitante', 'Habitante')
        Discapacidad = apps.get_model('DatosHabitante', 'HabitanteDiscapacidad')
        Vivienda = apps.get_model('DatosVivienda', 'Vivienda')

        # Reporte: Todos los habitantes que pertenecen a una etnia
        if tipo_reporte == "habitantes_etnia":
            qs = Habitante.objects.filter(pertenece_etnia=True)
            qd = Vivienda.objects.filter(id_vivienda=qs.first().id_vivienda.id_vivienda)
            qx = ConsejoComunal.objects.filter(id_consejo_comunal=qd.first().id_consejo_comunal_id)
            consejo = qx.first().nombre
            if comuna_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal__id_comuna=comuna_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
                "id_habitante",
                "cedula", 
                "primer_nombre", 
                "primer_apellido", 
                "sexo",
                "pertenece_etnia",
                "habitanteetnia__id_etnia__nombre"
            ))
            for item in data:
                item["Consejo_Comunal"] = consejo
            return Response({"tipo_reporte": "habitantes_etnia", "data": data}, status=200)
        
        # Reporte: Todos los habitantes con discapacidad
        elif tipo_reporte == "habitantes_discapacidad":
            qs = Habitante.objects.filter(discapacidad=True)
            qd = Vivienda.objects.filter(id_vivienda=qs.first().id_vivienda.id_vivienda)
            qx = ConsejoComunal.objects.filter(id_consejo_comunal=qd.first().id_consejo_comunal_id)
            consejo = qx.first().nombre
            if comuna_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal__id_comuna=comuna_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
                "id_habitante", 
                "cedula",
                "primer_nombre", 
                "primer_apellido", 
                "sexo"
                ))
            for item in data:
                item["Consejo_Comunal"] = consejo
            return Response({"tipo_reporte": "habitantes_discapacidad", "data": data}, status=200)
    
        # Reporte: Todos los habitantes con discapacidad específica
        elif tipo_reporte == "habitantes_discapacidad_especifica":
            discapacidad_nombre = request.data.get("discapacidad")
            qs = Habitante.objects.filter(
                discapacidad=True,
                habitantediscapacidad__id_tipo_discapacidad__nombre=discapacidad_nombre
            )
            qd = Vivienda.objects.filter(id_vivienda=qs.first().id_vivienda.id_vivienda)
            qx = ConsejoComunal.objects.filter(id_consejo_comunal=qd.first().id_consejo_comunal_id)
            consejo = qx.first().nombre
            
            if comuna_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal__id_comuna=comuna_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
                "id_habitante",
                "cedula",
                "primer_nombre",
                "primer_apellido",
                "sexo",
            ))
            # Add 'Consejo_Comunal' to each item in the data
            for item in data:
                item["Consejo_Comunal"] = consejo
            return Response({"tipo_reporte": "habitantes_discapacidad_especifica", "data": data}, status=200)

        # Reporte: Todos los habitantes de la tercera edad
        elif tipo_reporte == "habitantes_tercera_edad":
            hoy = date.today()
            fecha_limite = hoy.replace(year=hoy.year - 60)
            qs = Habitante.objects.filter(fecha_nacimiento__lte=fecha_limite)
            qd = Vivienda.objects.filter(id_vivienda=qs.first().id_vivienda.id_vivienda)
            qx = ConsejoComunal.objects.filter(id_consejo_comunal=qd.first().id_consejo_comunal_id)
            consejo = qx.first().nombre
            
            if comuna_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal__id_comuna=comuna_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
            "id_habitante",
            "cedula",
            "primer_nombre",
            "primer_apellido",
            "edad",
            "sexo"
            ))
            for item in data:
                item["Consejo_Comunal"] = consejo
            return Response({"tipo_reporte": "habitantes_tercera_edad", "data": data}, status=200)

        # Reporte: Todos los habitantes menores de edad
        elif tipo_reporte == "habitantes_menores_edad":
            hoy = date.today()
            try:
                fecha_limite = hoy.replace(year=hoy.year - 18)
            except ValueError:
                fecha_limite = hoy.replace(month=2, day=28, year=hoy.year - 18)
            qs = Habitante.objects.filter(fecha_nacimiento__gt=fecha_limite)
            qd = Vivienda.objects.filter(id_vivienda=qs.first().id_vivienda.id_vivienda)
            qx = ConsejoComunal.objects.filter(id_consejo_comunal=qd.first().id_consejo_comunal_id)
            consejo = qx.first().nombre
            
            if comuna_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal__id_comuna=comuna_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
                "id_habitante",
                "cedula",
                "primer_nombre",
                "primer_apellido",
                "edad",
                "sexo"
            ))
            for item in data:
                item["Consejo_Comunal"] = consejo
            return Response({"tipo_reporte": "habitantes_menores_edad", "data": data}, status=200)

        # Reporte: Todos los habitantes y su nivel de estudio
        elif tipo_reporte == "habitantes_nivel_estudio":
            qs = Habitante.objects.exclude(habitantenivelestudio=None)
            qd = Vivienda.objects.filter(id_vivienda=qs.first().id_vivienda.id_vivienda)
            qx = ConsejoComunal.objects.filter(id_consejo_comunal=qd.first().id_consejo_comunal_id)
            consejo = qx.first().nombre
   
            if comuna_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal__id_comuna=comuna_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
                "id_habitante",
                "cedula",
                "primer_nombre",
                "primer_apellido",
                "sexo",
                "habitantenivelestudio__id_nivel_estudio__nombre"
            ))
            for item in data:
                item["Consejo_Comunal"] = consejo
            return Response({"tipo_reporte": "habitantes_nivel_estudio", "data": data}, status=200)

        # Reporte: Todos los habitantes y su nivel de estudio específico
        elif tipo_reporte == "habitantes_nivel_estudio_especifico":
            nivel_nombre = request.data.get("nivel_estudio")
            qs = Habitante.objects.filter(
                habitantenivelestudio__id_nivel_estudio__nombre=nivel_nombre
            )
            qd = Vivienda.objects.filter(id_vivienda=qs.first().id_vivienda.id_vivienda)
            qx = ConsejoComunal.objects.filter(id_consejo_comunal=qd.first().id_consejo_comunal_id)
            consejo = qx.first().nombre
   
            if comuna_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal__id_comuna=comuna_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
                "id_habitante",
                "cedula",
                "primer_nombre",
                "primer_apellido",
                "sexo",
                "habitantenivelestudio__id_nivel_estudio__nombre"
            ))
            for item in data:
                item["Consejo_Comunal"] = consejo
            return Response({"tipo_reporte": "habitantes_nivel_estudio_especifico", "data": data}, status=200)

        # Reporte: Todas las viviendas con "x cantidad de habitantes"
        elif tipo_reporte == "viviendas_cantidad_habitantes":
            print("this got called")
            qs = Vivienda.objects.all()
            tipo_vivienda_id = request.data.get("id_tipo_vivienda")
            if tipo_vivienda_id:
                qs = qs.filter(id_tipo_vivienda=tipo_vivienda_id)
            if comuna_id:
                qs = qs.filter(id_consejo_comunal__id_comuna=comuna_id)
            data = list(qs.values("id_vivienda", "numero_vivienda", "cantidad_habitantes", "id_tipo_vivienda__descripcion"))
            return Response({"tipo_reporte": "viviendas_cantidad_habitantes", "data": data}, status=200)

        # Reporte: Todas las viviendas con "x cantidad de familias"
        elif tipo_reporte == "viviendas_cantidad_familias":
            qs = Vivienda.objects.all()
            if comuna_id:
                qs = qs.filter(id_consejo_comunal__id_comuna=comuna_id)
            data = list(qs.values("id_vivienda", "numero_vivienda", "cantidad_familias"))
            return Response({"tipo_reporte": "viviendas_cantidad_familias", "data": data}, status=200)
        
        # Reporte: Todas las viviendas de un tipo específico
        elif tipo_reporte == "viviendas_tipo":
            qs = Vivienda.objects.all()
            if comuna_id:
                qs = qs.filter(id_consejo_comunal__id_comuna=comuna_id)
            data = list(qs.values(
                "id_vivienda",
                "numero_vivienda",
                "id_tipo_vivienda__descripcion"
            ))
            return Response({"tipo_reporte": "viviendas_tipo", "data": data}, status=200)

        # Reporte: Todas las viviendas con "todos los tipos de techo"
        elif tipo_reporte == "viviendas_tipo_techo":
            qs = Vivienda.objects.all()
            if comuna_id:
                qs = qs.filter(id_consejo_comunal__id_comuna=comuna_id)
            data = list(qs.values(
                "id_vivienda",
                "numero_vivienda",
                "id_tipo_techo__descripcion"
                ).distinct())
            return Response({"tipo_reporte": "viviendas_tipo_techo", "data": data}, status=200)

        # Reporte: Todas las viviendas con "todos los tipos de piso"
        elif tipo_reporte == "viviendas_tipo_piso":
            qs = Vivienda.objects.all()
            if comuna_id:
                qs = qs.filter(id_consejo_comunal__id_comuna=comuna_id)
            data = list(qs.values(
                "id_vivienda",
                "numero_vivienda",
                "id_tipo_piso__descripcion"
            ))
            return Response({"tipo_reporte": "viviendas_tipo_piso", "data": data}, status=200)
        
        # Reporte: Todas las viviendas con "todos los tipos de pared"
        elif tipo_reporte == "viviendas_tipo_pared":
            qs = Vivienda.objects.all()
            if comuna_id:
                qs = qs.filter(id_consejo_comunal__id_comuna=comuna_id)
            data = list(qs.values(
                "id_vivienda",
                "numero_vivienda",
                "id_tipo_pared__descripcion"
            ))
            return Response({"tipo_reporte": "viviendas_tipo_pared", "data": data}, status=200)
        
        # Reporte: Todas las viviendas con "todas las situaciones de la vivienda"
        elif tipo_reporte == "viviendas_situacion":
            qs = Vivienda.objects.all()
            if comuna_id:
                qs = qs.filter(id_consejo_comunal__id_comuna=comuna_id)
            data = list(qs.values(
                "id_vivienda",
                "numero_vivienda",
                "id_situacion_vivienda__descripcion"
            ))
            return Response({"tipo_reporte": "viviendas_situacion", "data": data}, status=200)

        # Reporte: Todas las viviendas "ocupada / no ocupada"
        elif tipo_reporte == "viviendas_ocupacion":
            ocupada = request.data.get("ocupada")  # True/False o "true"/"false"
            if isinstance(ocupada, str):
                ocupada = ocupada.lower() == "true"
            qs = Vivienda.objects.filter(id_tipo_ocupacion_vivienda__vivienda_ocupada=ocupada)
            if comuna_id:
                qs = qs.filter(id_consejo_comunal__id_comuna=comuna_id)
            data = list(qs.values(
                "id_vivienda",
                "numero_vivienda",
            ))
            return Response({"tipo_reporte": "viviendas_ocupacion", "data": data}, status=200)

        else:
            return Response({"error": "Tipo de reporte no válido."}, status=400)


# Solo usuarios autenticados pueden acceder
@permission_classes([IsAuthenticated])
class ReporteParlamentario(ViewSet):
    def create(self, request):
        tipo_reporte = request.data.get("tipo_reporte")
        genero = request.data.get("genero")  # 'M' o 'F' o None
        consejo_comunal_id = request.data.get("consejo_comunal_id")  # ID del consejo comunal

        Habitante = apps.get_model('DatosHabitante', 'Habitante')
        Discapacidad = apps.get_model('DatosHabitante', 'HabitanteDiscapacidad')
        Vivienda = apps.get_model('DatosVivienda', 'Vivienda')

        # Reporte: Todos los habitantes que pertenecen a una etnia
        if tipo_reporte == "habitantes_etnia":
            qs = Habitante.objects.filter(pertenece_etnia=True)
            if consejo_comunal_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
                "id_habitante",
                "cedula", 
                "primer_nombre", 
                "primer_apellido", 
                "sexo", 
                "habitanteetnia__id_etnia__nombre"
            ))
            return Response({"tipo_reporte": "habitantes_etnia", "data": data}, status=200)
        
        # Reporte: Todos los habitantes con discapacidad
        elif tipo_reporte == "habitantes_discapacidad":
            qs = Habitante.objects.filter(discapacidad=True)
            if consejo_comunal_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
                "id_habitante", 
                "cedula",
                "primer_nombre", 
                "primer_apellido", 
                "sexo"
                ))
            return Response({"tipo_reporte": "habitantes_discapacidad", "data": data}, status=200)
    
        # Reporte: Todos los habitantes con discapacidad específica
        elif tipo_reporte == "habitantes_discapacidad_especifica":
            discapacidad_nombre = request.data.get("discapacidad")
            qs = Habitante.objects.filter(
                discapacidad=True,
                habitantediscapacidad__id_tipo_discapacidad__nombre=discapacidad_nombre
            )
            if consejo_comunal_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
                "id_habitante",
                "cedula",
                "primer_nombre",
                "primer_apellido",
                "sexo",
                "habitantediscapacidad__id_tipo_discapacidad__nombre"
            ))
            return Response({"tipo_reporte": "habitantes_discapacidad_especifica", "data": data}, status=200)

        # Reporte: Todos los habitantes de la tercera edad
        elif tipo_reporte == "habitantes_tercera_edad":
            hoy = date.today()
            fecha_limite = hoy.replace(year=hoy.year - 60)
            qs = Habitante.objects.filter(fecha_nacimiento__lte=fecha_limite)
            if consejo_comunal_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
            "id_habitante",
            "cedula",
            "primer_nombre",
            "primer_apellido",
            "edad",
            "sexo"
            ))
            return Response({"tipo_reporte": "habitantes_tercera_edad", "data": data}, status=200)

        # Reporte: Todos los habitantes menores de edad
        elif tipo_reporte == "habitantes_menores_edad":
            hoy = date.today()
            try:
                fecha_limite = hoy.replace(year=hoy.year - 18)
            except ValueError:
                # Para el 29 de febrero en años no bisiestos
                fecha_limite = hoy.replace(month=2, day=28, year=hoy.year - 18)
            qs = Habitante.objects.filter(fecha_nacimiento__gt=fecha_limite)
            if consejo_comunal_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
                "id_habitante",
                "cedula",
                "primer_nombre",
                "primer_apellido",
                "edad",
                "sexo"
            ))
            return Response({"tipo_reporte": "habitantes_menores_edad", "data": data}, status=200)

        # Reporte: Todos los habitantes y su nivel de estudio
        elif tipo_reporte == "habitantes_nivel_estudio":
            qs = Habitante.objects.exclude(habitantenivelestudio=None)
            if consejo_comunal_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
                "id_habitante",
                "cedula",
                "primer_nombre",
                "primer_apellido",
                "sexo",
                "habitantenivelestudio__id_nivel_estudio__nombre"
            ))
            return Response({"tipo_reporte": "habitantes_nivel_estudio", "data": data}, status=200)

        # Reporte: Todos los habitantes y su nivel de estudio específico
        elif tipo_reporte == "habitantes_nivel_estudio_especifico":
            nivel_nombre = request.data.get("nivel_estudio")
            qs = Habitante.objects.filter(
                habitantenivelestudio__id_nivel_estudio__nombre=nivel_nombre
            )
            if consejo_comunal_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
                "id_habitante",
                "cedula",
                "primer_nombre",
                "primer_apellido",
                "sexo",
                "habitantenivelestudio__id_nivel_estudio__nombre"
            ))
            return Response({"tipo_reporte": "habitantes_nivel_estudio_especifico", "data": data}, status=200)

        # Reporte: Todas las viviendas con "x cantidad de habitantes"
        elif tipo_reporte == "viviendas_cantidad_habitantes":
            tipo_vivienda_id = request.data.get("id_tipo_vivienda")
            qs = Vivienda.objects.all()
            if tipo_vivienda_id:
                qs = qs.filter(id_tipo_vivienda=tipo_vivienda_id)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values("id_vivienda", "numero_vivienda", "cantidad_habitantes", "id_tipo_vivienda__descripcion")) 
            return Response({"tipo_reporte": "viviendas_cantidad_habitantes", "data": data}, status=200)

        # Reporte: Todas las viviendas con "x cantidad de familias"
        elif tipo_reporte == "viviendas_cantidad_familias":
            qs = Vivienda.objects.all()
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values("id_vivienda", "numero_vivienda", "cantidad_familias"))
            return Response({"tipo_reporte": "viviendas_cantidad_familias", "data": data}, status=200)
        
        # Reporte: Todas las viviendas de un tipo específicos
        elif tipo_reporte == "viviendas_tipo":
            print("this called")
            tipo_vivienda_id = request.data.get("id_tipo_vivienda")
            print(tipo_vivienda_id)
            qs = Vivienda.objects.all()
            if tipo_vivienda_id:
                qs = qs.filter(id_tipo_vivienda=tipo_vivienda_id)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values(
                "id_vivienda",
                "numero_vivienda",
                "id_tipo_vivienda__descripcion"  # Trae el tipo de vivienda
            ))
            return Response({"tipo_reporte": "viviendas_tipo", "data": data}, status=200)

        # Reporte: Todas las viviendas con "todos los tipos de techo"
        elif tipo_reporte == "viviendas_tipo_techo":
            qs = Vivienda.objects.all()
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values(
                "id_vivienda",
                "numero_vivienda",
                "id_tipo_techo__descripcion"
                ).distinct())
            return Response({"tipo_reporte": "viviendas_tipo_techo", "data": data}, status=200)

        # Reporte: Todas las viviendas con "todos los tipos de piso"
        elif tipo_reporte == "viviendas_tipo_piso":
            qs = Vivienda.objects.all()
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values(
                "id_vivienda",
                "numero_vivienda",
                "id_tipo_piso__descripcion"
            ))
            return Response({"tipo_reporte": "viviendas_tipo_piso", "data": data}, status=200)
        
        # Reporte: Todas las viviendas con "todos los tipos de pared"
        elif tipo_reporte == "viviendas_tipo_pared":
            qs = Vivienda.objects.all()
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values(
                "id_vivienda",
                "numero_vivienda",
                "id_tipo_pared__descripcion"
            ))
            return Response({"tipo_reporte": "viviendas_tipo_pared", "data": data}, status=200)
        
        # Reporte: Todas las viviendas con "todas las situaciones de la vivienda"
        elif tipo_reporte == "viviendas_situacion":
            qs = Vivienda.objects.all()
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values(
                "id_vivienda",
                "numero_vivienda",
                "id_situacion_vivienda__descripcion"
            ))
            return Response({"tipo_reporte": "viviendas_situacion", "data": data}, status=200)

        # Reporte: Todas las viviendas "ocupada / no ocupada"
        elif tipo_reporte == "viviendas_ocupacion":
            ocupada = request.data.get("ocupada")  # True/False o "true"/"false"
            if isinstance(ocupada, str):
                ocupada = ocupada.lower() == "true"
            qs = Vivienda.objects.filter(id_tipo_ocupacion_vivienda__vivienda_ocupada=ocupada)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values(
                "id_vivienda",
                "numero_vivienda",
            ))
            return Response({"tipo_reporte": "viviendas_ocupacion", "data": data}, status=200)

        else:
            return Response({"error": "Tipo de reporte no válido."}, status=400)


# Solo usuarios autenticados pueden acceder
@permission_classes([IsAuthenticated])
class ReporteVocero(ViewSet):
    def create(self, request):
        tipo_reporte = request.data.get("tipo_reporte")
        genero = request.data.get("genero")  # 'M' o 'F' o None
        consejo_comunal_id = request.data.get("consejo_comunal_id")  # ID del consejo comunal

        Habitante = apps.get_model('DatosHabitante', 'Habitante')
        Discapacidad = apps.get_model('DatosHabitante', 'HabitanteDiscapacidad')
        Vivienda = apps.get_model('DatosVivienda', 'Vivienda')

        # Reporte: Todos los habitantes que pertenecen a una etnia
        if tipo_reporte == "habitantes_etnia":
            qs = Habitante.objects.filter(pertenece_etnia=True)
            if consejo_comunal_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
                "id_habitante",
                "cedula", 
                "primer_nombre", 
                "primer_apellido", 
                "sexo", 
                "habitanteetnia__id_etnia__nombre"
            ))
            return Response({"tipo_reporte": "habitantes_etnia", "data": data}, status=200)
        
        # Reporte: Todos los habitantes con discapacidad
        elif tipo_reporte == "habitantes_discapacidad":
            qs = Habitante.objects.filter(discapacidad=True)
            if consejo_comunal_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
                "id_habitante", 
                "cedula",
                "primer_nombre", 
                "primer_apellido", 
                "sexo"
                ))
            return Response({"tipo_reporte": "habitantes_discapacidad", "data": data}, status=200)
    
        # Reporte: Todos los habitantes con discapacidad específica
        elif tipo_reporte == "habitantes_discapacidad_especifica":
            discapacidad_nombre = request.data.get("discapacidad")
            qs = Habitante.objects.filter(
                discapacidad=True,
                habitantediscapacidad__id_tipo_discapacidad__nombre=discapacidad_nombre
            )
            if consejo_comunal_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
                "id_habitante",
                "cedula",
                "primer_nombre",
                "primer_apellido",
                "sexo",
                "habitantediscapacidad__id_tipo_discapacidad__nombre"
            ))
            return Response({"tipo_reporte": "habitantes_discapacidad_especifica", "data": data}, status=200)

        # Reporte: Todos los habitantes de la tercera edad
        elif tipo_reporte == "habitantes_tercera_edad":
            hoy = date.today()
            fecha_limite = hoy.replace(year=hoy.year - 60)
            qs = Habitante.objects.filter(fecha_nacimiento__lte=fecha_limite)
            if consejo_comunal_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
            "id_habitante",
            "cedula",
            "primer_nombre",
            "primer_apellido",
            "edad",
            "sexo"
            ))
            return Response({"tipo_reporte": "habitantes_tercera_edad", "data": data}, status=200)

        # Reporte: Todos los habitantes menores de edad
        elif tipo_reporte == "habitantes_menores_edad":
            hoy = date.today()
            try:
                fecha_limite = hoy.replace(year=hoy.year - 18)
            except ValueError:
                # Para el 29 de febrero en años no bisiestos
                fecha_limite = hoy.replace(month=2, day=28, year=hoy.year - 18)
            qs = Habitante.objects.filter(fecha_nacimiento__gt=fecha_limite)
            if consejo_comunal_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
                "id_habitante",
                "cedula",
                "primer_nombre",
                "primer_apellido",
                "edad",
                "sexo"
            ))
            return Response({"tipo_reporte": "habitantes_menores_edad", "data": data}, status=200)

        # Reporte: Todos los habitantes y su nivel de estudio
        elif tipo_reporte == "habitantes_nivel_estudio":
            qs = Habitante.objects.exclude(habitantenivelestudio=None)
            if consejo_comunal_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
                "id_habitante",
                "cedula",
                "primer_nombre",
                "primer_apellido",
                "sexo",
                "habitantenivelestudio__id_nivel_estudio__nombre"
            ))
            return Response({"tipo_reporte": "habitantes_nivel_estudio", "data": data}, status=200)

        # Reporte: Todos los habitantes y su nivel de estudio específico
        elif tipo_reporte == "habitantes_nivel_estudio_especifico":
            nivel_nombre = request.data.get("nivel_estudio")
            qs = Habitante.objects.filter(
                habitantenivelestudio__id_nivel_estudio__nombre=nivel_nombre
            )
            if consejo_comunal_id:
                qs = qs.filter(id_vivienda__id_consejo_comunal=consejo_comunal_id)
            if genero:
                qs = qs.filter(sexo=genero)
            data = list(qs.values(
                "id_habitante",
                "cedula",
                "primer_nombre",
                "primer_apellido",
                "sexo",
                "habitantenivelestudio__id_nivel_estudio__nombre"
            ))
            return Response({"tipo_reporte": "habitantes_nivel_estudio_especifico", "data": data}, status=200)

        # Reporte: Todas las viviendas con "x cantidad de habitantes"
        elif tipo_reporte == "viviendas_cantidad_habitantes":
            print("this got called")
            qs = Vivienda.objects.all()
            tipo_vivienda_id = request.data.get("id_tipo_vivienda")
            if tipo_vivienda_id:
                qs = qs.filter(id_tipo_vivienda=tipo_vivienda_id)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal__id_comuna=consejo_comunal_id)
            data = list(qs.values("id_vivienda", "numero_vivienda", "cantidad_habitantes", "id_tipo_vivienda__descripcion"))
            return Response({"tipo_reporte": "viviendas_cantidad_habitantes", "data": data}, status=200)

        # Reporte: Todas las viviendas con "x cantidad de familias"
        elif tipo_reporte == "viviendas_cantidad_familias":
            qs = Vivienda.objects.all()
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values("id_vivienda", "numero_vivienda", "cantidad_familias"))
            return Response({"tipo_reporte": "viviendas_cantidad_familias", "data": data}, status=200)
        
        # Reporte: Todas las viviendas de un tipo específico
        elif tipo_reporte == "viviendas_tipo":
            qs = Vivienda.objects.all()
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values(
                "id_vivienda",
                "numero_vivienda",
                "id_tipo_vivienda__descripcion"  # Trae el tipo de vivienda
            ))
            return Response({"tipo_reporte": "viviendas_tipo", "data": data}, status=200)

        # Reporte: Todas las viviendas con "todos los tipos de techo"
        elif tipo_reporte == "viviendas_tipo_techo":
            qs = Vivienda.objects.all()
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values(
                "id_vivienda",
                "numero_vivienda",
                "id_tipo_techo__descripcion"
                ).distinct())
            return Response({"tipo_reporte": "viviendas_tipo_techo", "data": data}, status=200)

        # Reporte: Todas las viviendas con "todos los tipos de piso"
        elif tipo_reporte == "viviendas_tipo_piso":
            qs = Vivienda.objects.all()
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values(
                "id_vivienda",
                "numero_vivienda",
                "id_tipo_piso__descripcion"
            ))
            return Response({"tipo_reporte": "viviendas_tipo_piso", "data": data}, status=200)
        
        # Reporte: Todas las viviendas con "todos los tipos de pared"
        elif tipo_reporte == "viviendas_tipo_pared":
            qs = Vivienda.objects.all()
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values(
                "id_vivienda",
                "numero_vivienda",
                "id_tipo_pared__descripcion"
            ))
            return Response({"tipo_reporte": "viviendas_tipo_pared", "data": data}, status=200)
        
        # Reporte: Todas las viviendas con "todas las situaciones de la vivienda"
        elif tipo_reporte == "viviendas_situacion":
            qs = Vivienda.objects.all()
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values(
                "id_vivienda",
                "numero_vivienda",
                "id_situacion_vivienda__descripcion"
            ))
            return Response({"tipo_reporte": "viviendas_situacion", "data": data}, status=200)

        # Reporte: Todas las viviendas "ocupada / no ocupada"
        elif tipo_reporte == "viviendas_ocupacion":
            ocupada = request.data.get("ocupada")  # True/False o "true"/"false"
            if isinstance(ocupada, str):
                ocupada = ocupada.lower() == "true"
            qs = Vivienda.objects.filter(id_tipo_ocupacion_vivienda__vivienda_ocupada=ocupada)
            if consejo_comunal_id:
                qs = qs.filter(id_consejo_comunal=consejo_comunal_id)
            data = list(qs.values(
                "id_vivienda",
                "numero_vivienda",
            ))
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
        Habitante = apps.get_model('DatosHabitante', 'Habitante')

    
        numero_habitantes = Habitante.objects.count()
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
