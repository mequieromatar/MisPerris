from django.urls import path
from Guau import views

urlpatterns = [
path('', views.index, name='index'),
path('formulario', views.form, name='formulario'),
path('login', views.forma, name='login'),
<<<<<<< HEAD
path('admin',views.admin, name="admin"),
path('Registro',views.regi, name="Registro")
=======
path('gestionPerros',views.admin, name="gestionPerros"),
>>>>>>> 51aeb774ebe798d2ce2bf01acd5507f406638d3a
]
