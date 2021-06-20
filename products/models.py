from django.db import models

# Create your models here.

class Productos(models.Model):
    ean=models.CharField(max_length=15)
    nombre=models.CharField(max_length=64)
    descripcion=models.CharField(max_length=200)
    precio=models.IntegerField()

    
    def __str__(self):
        return self.nombre

class Archivos(models.Model):
    nombre=models.CharField(max_length=100)
    cant_prod=models.IntegerField()
    prod_val=models.IntegerField()
    created=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre