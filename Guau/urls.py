from django.urls import path
from django.conf.urls import url
from Guau import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario', views.form, name='formulario'),
    path('login', views.ingre, name='login'),
    path('logout',views.salir, name='logout'),
    path('admin',views.admin, name="admin"),
    path('Registro',views.regi, name="Registro"),
    path('gestionPerros',views.registroPerro, name="gestionPerros"),
    path('listar',views.perroList, name="listarPerros"),
    path('galeria', views.Galeria, name="galeria"),
    path('recuperar',views.Recupera, name="recuperar"),
    url('editar/(?P<id>\d+)/$', views.Edita, name="editarPerros"),
    url('eliminar/(?P<id>\d+)/$', views.Eliminar, name="eliminarPerros"),
]
