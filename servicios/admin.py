from django.contrib import admin

from .models import Servicio,Registro
# register your models here.

class servicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    

    
admin.site.register(Servicio, servicioAdmin)

admin.site.register(Registro)
