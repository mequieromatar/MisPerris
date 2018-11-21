from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from Guau import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'home/', include(('Guau.urls', 'Guau'), namespace="Guau")),
    path('', RedirectView.as_view(url='/home/')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
