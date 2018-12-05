from django.shortcuts import render
from .models import usuario
from .serializers import usuarioSerializer
from rest_framework import viewsets
# Create your views here.


class usuarioView(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class  = usuarioSerializer
