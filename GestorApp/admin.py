
from import_export import resources

from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from .models import Conductor,Propietario,Sede, Encomienda,Vehiculo,Programacion



class ConductorResource(resources.ModelResource):
    fields = ('conductor', 'codigo', 'cedula','estado',)
    class Meta:
        model = Conductor

    def __str__(self):
        return str(self.conductor + ' - ' + self.codigo)

    class Meta:

        verbose_name_plural = 'Conductores'


# Register your models here.
@admin.register(Conductor)
class ConductorAdmin(ImportExportModelAdmin):
    list_display = ('conductor', 'codigo', 'cedula','estado',)
    search_fields = ('conductor', 'codigo', 'cedula','estado',)


class PropietarioResource(resources.ModelResource):
    fields = ('propietario', 'documento','estado', )
    class Meta:
        model = Propietario

    def __str__(self):
        return str(self.propietario)

    class Meta:
        verbose_name_plural = 'Propietarios'



@admin.register(Propietario)
class PropietarioAdmin(ImportExportModelAdmin):
    list_display =('propietario', 'documento','estado',)
    search_fields = ('propietario','documento','estado',)


class SedeResource(resources.ModelResource):
    fields = ('conductor', 'codigo', 'cedula','estado',)
    class Meta:
        model = Sede
    def __str__(self):
        return str(self.sede + ' - ' + self.tipo)



@admin.register(Sede)
class SedeAdmin(ImportExportModelAdmin):
    list_display = ('sede','tipo', 'fecha_creado','fecha_actualizado')
    list_filter = ['sede','tipo']
    search_fields = ['sede','tipo']


@admin.register(Vehiculo)
class VehiculoAdmin(ImportExportModelAdmin):
    list_display =('propietario','numero_veh','placa_veh','asientos','estado','fecha_creado','fecha_actualizado',)
    list_filter = ['propietario','numero_veh',]
    search_fields = ['propietario','numero_veh']
@admin.register(Programacion)
class ProgramacionAdmin(ImportExportModelAdmin):
    list_display = ('codigo','vehiculo', 'conductor', 'origen', 'destino', 'programacion','precio', 'estado','fecha_creado','fecha_actualizado', )
    list_filter = ['codigo', 'vehiculo', 'origen','destino',]
    search_fields = ['codigo', 'vehiculo', 'programacion']

@admin.register(Encomienda)
class EncomiendaAdmin(ImportExportModelAdmin):
    list_display =('programacion', 'nombre_envio','cedula_envio','cedula_envio','telefono_envio','nombre_recibido',
                   'cedula_recibido','telefono_recibido','costo_envio','estado','fecha_creado','fecha_actualizado',)
    list_filter =['programacion','estado',]
    search_fields =['nombre_envio','cedula_envio','cedula_envio','telefono_envio','nombre_recibido','cedula_recibido','telefono_recibido', 'estado',]