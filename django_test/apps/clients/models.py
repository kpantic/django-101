from django.db import models

# Create your models here.

class Cliente(models.Model):
	cedula = models.CharField('Cedula', max_length=10, unique=True)
	nombre = models.CharField('Nombre', max_length=256)
	direccion = models.TextField('Direccion')

class Producto(models.Model):
	nombre = models.CharField('Nombre Producto', max_length=256)
	cliente = models.ForeignKey(Cliente, related_name="productos") 