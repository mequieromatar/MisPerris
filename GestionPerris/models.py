from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class usuario(models.Model):
    id_usuario = models.AutoField(max_length=6, primary_key=True)
    email_usuario = models.CharField(max_length=40, null=False)
    run_usuario = models.CharField(max_length=10, primary_key=True)
    nombre_usuario = models.CharField(max_length=50, null=False)
    fechanac_usuario = models.DateField(null=False)
    contra = models.CharField(max_length=30, null=False)
    id_tipo = models.CharField(max_length=1, null=False)


class cliente(models.Model):
    id_cliente = models.AutoField(max_length=3, primary_key=True)
    nombre_cliente = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=40,null=False)
    ciudad = models.CharField(max_length=50, null=False)
    comunas = models.CharField(max_length=40, null=False)
    telefono = models.CharField(max_length=10, null=False)
    correo = models.CharField(max_length=50, null=False)

class ordendetrabajo(models.Model):
    id_orden = models.AutoField(max_length=6, primary_key=True)
    id_cliente = models.ForeignKey(cliente,on_delete=models.CASCADE)
    run_cliente = models.ForeignKey(cliente,on_delete=models.CASCADE)
    nombre_cliente = models.ForeignKey(cliente,on_delete=models.CASCADE)
    fecha = models.DateField(null=False)
    hora_ini = models.DateField(null=False)
    hora_term = models.DateField(null=False)
    id_ascensor = models.CharField(max_length=10, null=False)
    modelo_ascensor = models.CharField(max_length=20, null=False)
    descripcion_falla = models.CharField(max_length=300, null=True)
    descripcion_reparacion = models.CharField(max_length=300, null=True)
    piezas_cambiadas = models.CharField(max_length=200, null=True)
    nombre_receptor = models.CharField(max_length=50, null=True)
    id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
