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
        forma = adoptanteForm(request.POST)
        print('Resultado :',request.POST)
        if forma.is_valid():
            print('Es valido')
            forma.save()
            return redirect('Guau:formulario')
        else:
            print(forma.errors)
            formita = adoptanteForm()
        #Este es el formulario del postulante
    return render(request, 'index.html')

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
