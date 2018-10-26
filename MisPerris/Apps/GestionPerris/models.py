from django.db import models

# Create your models here.

class perro(models.Model):
    id_perro = models.CharField(max_length=5, primary_key=True, default='0')
    foto = models.ImageField()
    nombre_perro = models.CharField(max_length=30)
    raza_predom = models.CharField(max_length=30)
    descrip = models.CharField(max_length=30)
    estados = (('R','Rescatado'),('D','Disponible'),('A','adoptado'))
    estado = models.CharField(max_length=1, choices=estados, default='R')

class adoptante(models.Model):
    email_usuario = models.CharField(max_length=40)
    run_usuario = models.CharField(max_length=10, help_text="run", primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    fono_usuario= models.CharField(max_length=9)
    fechanac_usuario = models.DateField()
    regiones = models.CharField(max_length=20)
    comunas = models.CharField(max_length=20)
    tipo_viviendas = (('G','Casa con patio grande'),
    ('P','Casa con patio grande'),('S','Casa sin patio'),('D','Departamento'))
    tipo_vivienda = models.CharField(max_length=1, choices=tipo_viviendas, default='G')
