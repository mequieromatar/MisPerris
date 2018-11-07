from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from GestionPerris.Forms import adoptanteForm, usuarioUwuForm, perroForm
from GestionPerris.models import adoptante, usuarioUwu, perro

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
        return render(request, 'admin/gestionPerros.html')

def regi(request):
        if request.method == "POST":
            formita = usuarioUwuForm(request.POST)
            print('Resultado :',request.POST)
            if formita.is_valid():
                print('Es valido')
                formita.save()
                return redirect('Guau:Registro')
            else:
                print(formita.errors)
                formita = usuarioUwuForm()
        return render(request, 'Registro.html')

def registroPerro(request):
    # Registro de perros
        if request.method == "POST":
            formita = perroForm(request.POST, request.FILES)
            print('Resultado :',request.POST, request.FILES)
            if formita.is_valid():
                print('Es valido')
                formita.save()
                return redirect('Guau:registroPerro')
            else:
                print(formita.errors)
                formita = perroForm()
        return render(request, 'Admin/gestionPerros.html')

def perroList(request):
    # Listado de los Perros
    perro = Perro.object.all()
    contexto = {'perros':perros}
    return render(request,'Templates/Admin/gestionPerros.html',contexto)
