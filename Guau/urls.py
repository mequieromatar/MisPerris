from django.urls import path
from django.conf.urls import url
from Guau import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

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
  path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/< uidb64 >/< token >',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ),
         name='password_reset_complete'),]
