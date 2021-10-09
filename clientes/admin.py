from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db.models.base import Model
from .models import Cliente, Factura, Parqueadero, Puesto, Vehiculo, Reserva
# Register your models here.

admin.site.register(Cliente)
#admin.site.register(Factura)
#admin.site.register(Parqueadero)
admin.site.register(Vehiculo)


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ("id","hora_llegada","hora_salida","placa_vehiculo","nombre_administrativo","tipo_vehiculo","dueño_vehiculo","total_vehiculo")

@admin.register(Parqueadero)
class ParqueaderoAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_administrador","ubicacion","placa_vehiculo","gastos_totales","hora_puesto")

    
    
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("id","placa","hora_llegada")
    
@admin.register(Puesto)
class PuestoAdmin(admin.ModelAdmin):
    list_display = ("puestos_totales","puestos_llenos", "puestos_vacios")
