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

class adoptante(models.Model):

    email_usuario = models.CharField(max_length=40, null=False)
    run_usuario = models.CharField(max_length=10, primary_key=True)
    nombre_usuario = models.CharField(max_length=50, null=False)
    fono_usuario= models.CharField(max_length=9, null=False)
    fechanac_usuario = models.DateField(null=False)
    regiones = models.CharField(max_length=40, null=False)
    comunas = models.CharField(max_length=40, null=False)
    tipo_viviendas = ((1,'Casa con patio grande'),(2,'Casa con patio pequeño'),(3,'Mercedes'),(4,'Departamento'))
    tipo_vivienda = models.IntegerField(choices=tipo_viviendas)

class usuarioUwu(models.Model):
        usuario = models.OneToOneField(User, on_delete=models.CASCADE)
        email_usuario = models.CharField(max_length=40)
        uname = models.CharField(max_length=50, primary_key=True)
        psw = models.CharField(max_length=40, null=False)
        tipo_usuario = ((1,'administrador'),(2, 'adoptante'))
        tip = models.IntegerField(choices=tipo_usuario,default=2)
