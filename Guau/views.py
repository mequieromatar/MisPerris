from django.shortcuts import render

# Create your views here.
def index(request):
    # Vista principal de los perris
    return render(request, 'misperritos.html')

def form(request):
    # Este es el formulario del postulante
    return render(request, 'Index.html')

def form(request):
    # Este es el login
    return render(request, 'Login.html')
