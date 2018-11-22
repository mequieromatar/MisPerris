from .models import usuarioUwu
from rest_framework import serializers



class uwuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = usuarioUwu
        fields = ('email_usuario', 'uname')
