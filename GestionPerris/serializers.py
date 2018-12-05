from .models import usuario
from rest_framework import serializers



class usuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = usuario
        fields = ('email_usuario', 'contra')
