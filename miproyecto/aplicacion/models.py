from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=80)
    autor = models.CharField(max_length=60)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    genero = models.CharField(max_length=40)
    celContacto = models.IntegerField()
    emailContacto = models.EmailField()

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    contraseña = models.CharField(max_length=10)

class Comentario(models.Model):
    texto = models.CharField(max_length=100)
    usuario = models.CharField(max_length=80)