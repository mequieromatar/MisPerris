from django.shortcuts import render
from .models import usuarioUwu
from .serializers import uwuarioSerializer
from rest_framework import viewsets
# Create your views here.


class usuarioViewuwu(viewsets.ModelViewSet):
    queryset = usuarioUwu.objects.all()
    serializer_class  = uwuarioSerializer
