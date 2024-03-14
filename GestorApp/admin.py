
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from .models import Conductor,Sede, Propietario,Encomienda,Vehiculo,Programacion

from import_export import resources


# Register your models here.
admin.site.register(Sede)
admin.site.register(Vehiculo)


class ConductorResource(resources.ModelResource):
    fields = ('conductor', 'codigo', 'cedula','estado',)
    class Meta:
        model = Conductor
        verbose_name_plural = 'Conductores'
    def __str__(self):
        return str(self.conductor + ' - ' + self.codigo)



@admin.register(Conductor)
class ConductorAdmin(ImportExportModelAdmin):
    recourse_class = ConductorResource
    list_display = ('conductor', 'codigo', 'cedula','estado',)

    def admin_conductor(self, obj):
        return 'Conductores'

    search_fields = ('conductor', 'codigo', 'cedula','estado',)


class PropietarioResource(resources.ModelResource):
    fields = ('propietario', 'documento','estado', )
    class Meta:
        model = Propietario

    def __str__(self):
        return str(self.propietario)

    class Meta:
        verbose_name_plural = 'Propietarios'
#conductor model recourse


@admin.register(Propietario)
class PropietarioAdmin(ImportExportModelAdmin):
    recourse_class = PropietarioResource
    list_display =('propietario', 'documento','estado',)

    def admin_propietario(self, obj):
        return 'Propietarios'

    search_fields = ('propietario','documento','estado',)


admin.site.register(Programacion)


#### exportar####
class ProgramacionResource(resources.ModelResource):

    class Meta:
        model = Programacion
        fields = ('codigo', 'vehiculo','conductor','origen','destino','programacion','precio','estado', 'fecha_creado', "fecha_actualizado",)
        export_order = ('codigo', 'vehiculo','conductor','origen','destino','programacion','precio','estado', 'fecha_creado', "fecha_actualizado",)



admin.site.register(Encomienda)