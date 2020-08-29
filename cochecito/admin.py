from django.contrib import admin
from .models import Marca , Automovil

# Register your models here.

#segunda configuracion se agrego la clase AutomovilAdmin

class AutomovilAdmin(admin.ModelAdmin):
    list_display=('placa','marca','anio','modelo')
    #search se usa como buscar
    search_fields= ['placa','modelo']
    #filter se usa para filtrar
    list_filter=("marca",)

#Primera configuracion
#admin.site.register(Marca)
admin.site.register(Marca)
#admin.site.register(Automovil)
admin.site.register(Automovil,AutomovilAdmin)

#se agrego AutomovilAdmin 
#para poner mas campos personalizar la funcionalidad del admin
#declarar clase de configuracion para la entidad a extender




