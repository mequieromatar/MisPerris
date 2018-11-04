from django.db import models

# Create your models here.

class perro(models.Model):
    id_perro = models.CharField(max_length=5, primary_key=True, default='0')
    #foto = models.ImageField(null=True)
    nombre_perro = models.CharField(max_length=30, null=False)
    raza_predominante = models.CharField(max_length=30, null=False)
    descripcion = models.CharField(max_length=30, null=False)
    estados = (('R','Rescatado'),('D','Disponible'),('A','adoptado'))
    estado = models.CharField(max_length=1, choices=estados, default='R', null=False)

class adoptante(models.Model):
    email_usuario = models.CharField(max_length=40, null=False)
    run_usuario = models.CharField(max_length=10, primary_key=True)
    nombre_usuario = models.CharField(max_length=50, null=False)
    fono_usuario= models.CharField(max_length=9, null=False)
    fechanac_usuario = models.DateField(null=False)
    regiones = models.CharField(max_length=20, null=False)
    comunas = models.CharField(max_length=20, null=False)
    tipo_viviendas = (('G','Casa con patio grande'),
    ('P','Casa con patio grande'),('S','Casa sin patio'),('D','Departamento'))
    tipo_vivienda = models.CharField(max_length=1, choices=tipo_viviendas, default='G', null=False)
