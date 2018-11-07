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
#login
def ingre(request):
    form=usuarioUwuForm(request.POST)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(uname=data.get("uname"),psw=data.get("psw"))
        if user is not None:
            login(request,user)
            return redirect('Guau:login')
    return render(request,"login.html")
#logout
def salir(request):
    logout(request)
    return redirect("/")

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
                return redirect('Guau:listarPerros')
            else:
                print(formita.errors)
                formita = perroForm()
        return render(request, 'Admin/gestionPerros.html')

def perroList(request):
    # Listado de los Perros
    perris = perro.objects.all()
    contexto = {'perros':perris}
    return render(request,'Admin/listarPerros.html',contexto)

def perroEdit(request, id_perro):
    perris = perro.objects.get(id=id_perro)
    if request.method == 'GET':
        form = perroForm(instance=perris)
    else:
        form = perroForm(request.POST, instance=perris)
        if form.is_valid:
            form.save()
        return redirect('Guau:listarPerros')
    return render(request, 'Admin/gestionPerros.html', {'form':form})
