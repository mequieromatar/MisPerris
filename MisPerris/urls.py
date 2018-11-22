from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from Guau import views
from django.contrib.auth import views as auth_views
from GestionPerris.views import usuarioViewuwu
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Veruwusuarios',usuarioViewuwu)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'home/', include(('Guau.urls', 'Guau'), namespace="Guau")),
    path('', RedirectView.as_view(url='/home/')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
	  path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='reset/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    url(r'^', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
