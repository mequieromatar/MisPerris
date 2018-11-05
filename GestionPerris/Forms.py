from django import forms

class perroForm(forms.Form):
    id_perro = forms.CharField()
    #foto = models.ImageField(null=True)
    nombre_perro = forms.CharField()
    raza_predominante = forms.CharField()
    descripcion = forms.CharField()
    estados = (('R','Rescatado'),('D','Disponible'),('A','adoptado'))
    estado = forms.CharField()

class adoptanteForm(forms.Form):
    email_usuario = forms.CharField()
    run_usuario = forms.CharField()
    nombre_usuario = forms.CharField()
    fono_usuario= forms.CharField()
    fechanac_usuario = forms.DateField()
    comunas = forms.CharField()
    regiones = forms.CharField()
    tipo_viviendas = (('G','Casa con patio grande'),
    ('P','Casa con patio grande'),('S','Casa sin patio'),('D','Departamento'))
    tipo_vivienda = forms.CharField()

class usuarioUwuForm(forms.Form):
        email_usuario =forms.CharField()
        uname = forms.CharField()
        psw = forms.CharField()
        tipo_usuario = (('1','administrador'),('2', 'adoptante'))
        tip = forms.CharField()
