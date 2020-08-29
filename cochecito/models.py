from django.db import models

# Create your models here.

class Marca(models.Model):
    #django agrega id(autoIncrementable) a todos los modelos de manera nativa
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

# funcion __str__ se usa para quitar Marca.object(1) y aparezca lo que se guardo (nombre)
    def __str__(self):
        return self.nombre


class Automovil(models.Model):
    placa = models.CharField(max_length=10 , unique=True)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField(verbose_name="año")
    #anio = models.IntegerField() se usa verbose_name para reescribir
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    #se agrega las siguientes lineas de codigo para subir imagenes
    #las imagenes iran en la carpeta automoviles
    imagen = models.ImageField(upload_to="automoviles" , null=True)


# funcion __str__ se usa para quitar Marca.object(1) y aparezca lo que se guardo (placa)
    def __str__(self):
        return self.placa

# Class Meta con verbose_name cambiamos el nombre de automovils por Automoviles 
    class Meta():
        verbose_name = "Automovil"
        verbose_name_plural : "Automoviles"