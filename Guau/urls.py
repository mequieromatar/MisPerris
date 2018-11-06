from django.urls import path
from Guau import views

urlpatterns = [
path('', views.index, name='index'),
path('formulario', views.form, name='formulario'),
path('login', views.forma, name='login'),
path('admin',views.admin, name="admin"),
path('Registro',views.regi, name="Registro"),
path('gestionPerros',views.admin, name="gestionPerros"),

]
