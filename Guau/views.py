from django.shortcuts import render
from django.contrib.auth import views as auth_views
<<<<<<< HEAD
from GestionPerris.Forms import adoptanteForm, usuarioUwuForm
from GestionPerris.models import adoptante, usuarioUwu
=======
from GestionPerris.forms import adoptanteForm
from GestionPerris.models import adoptante
>>>>>>> 51aeb774ebe798d2ce2bf01acd5507f406638d3a
# Create your views here.
def index(request):
    # Vista principal de los perris
    return render(request, 'misperritos.html')

def form(request):
    if request.method == "POST":
        form = adoptanteForm(request.POST)
        if form.is_valid():
            email_usuario = request.POST.get('email_usuario','')
            run_usuario = request.POST.get('run_usuario','')
            nombre_usuario = request.POST.get('nombre_usuario','')
            fono_usuario = request.POST.get('fono_usuario','')
            fechanac_usuario = request.POST.get('fechanac_usuario','')
            regiones = request.POST.get('regiones','')
            comunas = request.POST.get('comunas','')
            tipo_vivienda = request.POST.get('tipo_vivienda','')
            adoptante_obj = adoptante(email_usuario = email_usuario, run_usuario = run_usuario, nombre_usuario = nombre_usuario, fono_usuario = fono_usuario,
            fechanac_usuario = fechanac_usuario, regiones = regiones, comunas = comunas, tipo_vivienda = tipo_vivienda )
            adoptante_obj.save()

        else:
            form = adoptante_obj('adoptante')
    # Este es el formulario del postulante
    return render(request, 'Index.html')

def forma(request):
    # Este es el login
    return render(request, 'Login.html')

def admin(request):
    # Alfa el jefe
<<<<<<< HEAD
    return render(request, 'Admin.html')

def regi(request):
    if request.method == "POST":
         forma = usuarioUwuForm(request.POST)
            if forma.is_valid():
                uname = request.POST.get('uname','')
                email_usuario = request.POST.get('email_usuario','')
                psw = request.POST.get('psw','')
                tip = request.POST.get('tip','1')
                usuario_obj = usuarioUwu(uname = uname, email_usuario = email_usuario, psw = psw, tip = tip)
                usuario_obj.save()
            else:
                forma= usuario_obj('usuarioUwu')


            return render(request, 'Registro.hmtl')
=======
    return render(request, 'admin/gestionPerros.html')
>>>>>>> 51aeb774ebe798d2ce2bf01acd5507f406638d3a
