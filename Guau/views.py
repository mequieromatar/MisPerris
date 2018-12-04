from django.shortcuts import render, redirect
from django.contrib import auth
from GestionPerris.Forms import *
from GestionPerris.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.


def index(request):
    # Vista principal de los perris
    return render(request, 'misperritos.html')



def form(request):
    if request.method == "POST":
        forma = adoptanteForm(request.POST)
        print('Resultado :', request.POST)
        if forma.is_valid():
            print('Es valido')
            forma.save()
            return redirect('Guau:formulario')
        else:
            print(forma.errors)
            formita = adoptanteForm()
        # Este es el formulario del postulante
    return render(request, 'index.html')


# login
def ingre(request):
    if request.user.is_authenticated:
        return redirect('Guau:index')
    else:
        if request.method=="POST":
            print('valido')
            user = auth.authenticate(username=request.POST.get("uname"), password=request.POST.get("psw"))
            print(user)
            if user is not None:
                print(user.is_staff)
                auth.login(request, user)
                request.session.set_expiry(60)
                if request.user.is_staff:
                    messages.success(request, 'Se ha ingresado con exito')
                    return  redirect('Guau:gestionPerros')
                else:
                    return redirect('Guau:index')
            else:
                messages.error(request,'El nombre de usuario y/o contraseña es incorrecta')
        return render(request, "login.html")

# logout
def salir(request):
    auth.logout(request)
    messages.success(request,'Se ha cerrado su sesion con exito')
    return redirect("/home/login")


def admin(request):
    # Alfa el jefe
    return render(request, 'admin/gestionPerros.html')


def regi(request):
    if request.method == "POST":
        formita = usuarioUwuForm(request.POST)
        print('Resultado :', request.POST)
        if formita.is_valid():
            print('Es valido')
            data = formita.cleaned_data
            u = User.objects.create_user(data.get("uname"), data.get("email_usuario"), data.get("psw"))
            u.is_staff = False
            u.save()
            usuario = usuarioUwu(uname=data.get("uname"), email_usuario=data.get("email_usuario"), psw=data.get("psw"), usuario=u)
            usuario.save()
            return redirect('Guau:Registro')
        else:
            print(formita.errors)
            formita = usuarioUwuForm()
    return render(request, 'Registro.html')


def registroPerro(request):
    # Registro de perros
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == "POST":
                formita = perroForm(request.POST, request.FILES)
                print('Resultado :', request.POST, request.FILES)
                if formita.is_valid():
                    print('Es valido')
                    formita.save()
                    messages.success(request, 'Perrito registrado con exito')
                    return redirect('Guau:listarPerros')
                else:
                    print(formita.errors)
                    formita = perroForm()
                    messages.error(request, 'No se logro registrar al perrito')
            return render(request, 'Admin/gestionPerros.html')
        else:
            return redirect('Guau:index')
    else:
        return redirect('Guau:login')

def perroList(request):
    # Listado de los clientes
    if request.user.is_authenticated:
        if request.user.is_staff:
            cliente = cliente.objects.all()
            contexto = {'clientes':cliente}
            return render(request,'Admin/listarPerros.html', contexto)
        else:
            return redirect('Guau:index')
    else:
        return redirect('Guau:index')

def perroList(request):
    # Listado de los usuarios
    if request.user.is_authenticated:
        if request.user.is_staff:
            usuario = usuario.objects.all()
            contexto = {'usuarios':usuario}
            return render(request,'Admin/listarUsuarios.html', contexto)
        else:
            return redirect('Guau:index')
    else:
        return redirect('Guau:index')


def Edita(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            perris = perro.objects.get(id_perro=id)
            if request.method == 'GET':
                form = perroForm(instance=perris)
            else:
                form = perroForm(request.POST, instance=perris)
                if form.is_valid:
                    form.save()
                    messages.success(request, 'Perro editado con exito')
                return redirect('Guau:listarPerros')
            return render(request, 'Admin/Editar.html', {'form':form})
        else:
            return redirect('Guau:index')
    else:
        return redirect('Guau:login')



def Recupera(request):
    return render(request, 'Recuperar.html')

def Eliminar(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            perris = perro.objects.get(id_perro=id)
            if request.method == 'POST':
                perris.delete()
                messages.error(request, 'Perro eliminado')
                return redirect('Guau:listarPerros')
            return render(request, 'Admin/eliminar.html', {'form':form})
        else:
            return redirect('Guau:index')
    else:
        return redirect('Guau:login')

def LogOut(request):
    logout(request)
    return redirect('/home/login')

def ListaCliente(request):
    perris = perro.objects.all()
    contexto = {'perros':perris}
    return render(request,'Cliente/listado.html', contexto)
