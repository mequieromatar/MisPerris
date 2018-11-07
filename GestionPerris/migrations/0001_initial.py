# Generated by Django 2.1.2 on 2018-11-07 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='adoptante',
            fields=[
                ('email_usuario', models.CharField(max_length=40)),
                ('run_usuario', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('fono_usuario', models.CharField(max_length=9)),
                ('fechanac_usuario', models.DateField()),
                ('regiones', models.CharField(max_length=40)),
                ('comunas', models.CharField(max_length=40)),
                ('tipo_vivienda', models.IntegerField(choices=[(1, 'Casa con patio grande'), (2, 'Casa con patio pequeño'), (3, 'Mercedes'), (4, 'Departamento')])),
            ],
        ),
        migrations.CreateModel(
            name='perro',
            fields=[
                ('id_perro', models.AutoField(max_length=5, primary_key=True, serialize=False)),
                ('foto', models.ImageField(null=True, upload_to='')),
                ('nombre_perro', models.CharField(max_length=30)),
                ('raza_predominante', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
                ('estado', models.CharField(choices=[('R', 'Rescatado'), ('D', 'Disponible'), ('A', 'Adoptado')], default='R', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='usuarioUwu',
            fields=[
                ('email_usuario', models.CharField(max_length=40)),
                ('uname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('psw', models.CharField(max_length=40)),
                ('tip', models.IntegerField(choices=[(1, 'administrador'), (2, 'adoptante')], default=2)),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
