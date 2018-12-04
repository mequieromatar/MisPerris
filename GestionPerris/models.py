from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class perro(models.Model):
    id_perro = models.AutoField(max_length=5, primary_key=True)
    foto = models.ImageField(null=True)
    nombre_perro = models.CharField(max_length=30, null=False)
    raza_predominante = models.CharField(max_length=30, null=False)
    descripcion = models.CharField(max_length=30, null=False)
    estados = (('R','Rescatado'),('D','Disponible'),('A','Adoptado'))
    estado = models.CharField(max_length=1, choices=estados, default='R', null=False)

class usuario(models.Model):

    email_usuario = models.CharField(max_length=40, null=False)
    run_usuario = models.CharField(max_length=10, primary_key=True)
    nombre_usuario = models.CharField(max_length=50, null=False)
    fechanac_usuario = models.DateField(null=False)
    contra = models.CharField(max_length=30, null=False)
    id_tipo = models.CharField(max_length=1, null=False)


class tipo_usuario(models.Model):
    id_tipo = models.CharField(max_length=1, primary_key=True)
    desc = models.CharField(max_length=12, null=False)

class cliente(models.Model):
    
