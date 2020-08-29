

from django.urls import path
from .views import home, galeria, formulario, listar_automoviles, eliminar_automoviles, modificar_automovil

urlpatterns = [
    path('', home, name="home"),
    path('galeria/',galeria, name="galeria"),
    path('formulario/',formulario, name="formulario"),
    path('listar-autos/',listar_automoviles,name="listado_automoviles"),
    path('eliminar-auto/<id>/',eliminar_automoviles, name="eliminar_automovil"),
    path('modificar-auto/<id>',modificar_automovil, name="modificar_automovil")
    
]