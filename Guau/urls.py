from django.urls import path
from Guau import views

urlpatterns = [
path('', views.index, name='index'),
path('formulario', views.form, name='formulario'),
path('login', views.forma, name='login'),
path('gestionPerros',views.admin, name="gestionPerros"),
]
