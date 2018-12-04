from django import forms
from .models import *



class usuarioForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ('email_usuario','run_usuario','nombre_usuario',
        'fechanac_usuario','contra','id_tipo')

class clienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ('id_cliente','nombre_cliente','direccion','ciudad','comunas','telefono','correo')

class loginForm(forms.ModelForm):
    class Meta:
        model = usuarioUwu
        fields = ('uname', 'psw')

class ordendetrabajoForm(forms.ModelForm):
    class Meta:
        model = ordendetrabajo
        fields = ('id_orden','id_cliente','run_cliente','nombre_cliente','fecha','hora_ini','hora_term','id_ascensor','modelo_ascensor','descripcion_falla',
        'descripcion_reparacion','piezas_cambiadas','nombre_receptor', 'id_usuario')
