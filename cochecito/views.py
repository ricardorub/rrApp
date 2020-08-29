from django.shortcuts import render , redirect
from .models import Marca , Automovil
# se agrego redirect y messages
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request , 'cochecito/home.html')

def galeria(request):
    return render(request , 'cochecito/galeria.html')

def formulario(request):

    marcas = Marca.objects.all()
    variables = {
        'marcas': marcas
    }

    if request.POST:
        #instanciar un Automovil
        auto = Automovil()
        auto.placa = request.POST.get('txtPlaca')
        auto.marca = request.POST.get('txtMarca')
        auto.anio = request.POST.get('txtAnio')
        auto.modelo= request.POST.get('txtModelo')
        #linea de codigo para la imagen
        auto.imagen= request.FILES.get('txtImagen')
        # instanciamos una Marca
        marca = Marca()
        marca.id = request.POST.get('cboMarca')
        #dejamos el objeto marca dentro del auto
        auto.marca = marca
        #teniendo todos los datos capturados desde
        #el template , guardamos el automovil en la base de datos

        try:
            auto.save()
            variables['mensajes'] = 'Guardado correctamente'
        except:
            variables['mensajes'] = 'No se ha podido guardar'

    return render(request , 'cochecito/formulario.html', variables)


#CRUD de automovil
def listar_automoviles(request):
    
    autos = Automovil.objects.all()
    return render(request ,'cochecito/listar_automoviles.html',{'autos':autos})
    #autos se pasa como una variable pero se pasa a un 
    #diccionario para que trabaje sin error

def eliminar_automoviles(request , id):
    #buscar el automovil que queremos eliminar
    auto = Automovil.objects.get(id=id)

    try:
        auto.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje= "no se ha podido eliminar"
        messages.error(request, mensaje)

    return redirect('listado_automoviles')
    #redireje con el alias listado_automoviles

def modificar_automovil(request,id):
    #buscamos el automovil para que el usuario lo pueda modificar
    auto = Automovil.objects.get(id=id)
    marcas = Marca.objects.all()
    variables = {
        'auto':auto ,
        'marcas':marcas
    }

    if request.POST:
        auto = Automovil()
        auto.id = request.POST.get('txtId')
        auto.placa = request.POST.get('txtPlaca')
        auto.marca = request.POST.get('txtMarca')
        auto.anio = request.POST.get('txtAnio')
        auto.modelo= request.POST.get('txtModelo')
        
        marca = Marca()
        marca.id = request.POST.get('cboMarca')
        auto.marca = marca

        try:
            auto.save()
            messages.success(request ,'modificado correctamente')
            #mensaje va por framework de django
        except:
            messages.error(request , 'no se ha podido modificar')
        return redirect('listado_automoviles')

    return render(request,'cochecito/modificar_automovil.html',variables)


