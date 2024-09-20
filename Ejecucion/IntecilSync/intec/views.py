from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def formularioVisa(request):
    return render(request, 'visa/formularioVisa.html')


@login_required
def inicio(request):
    return render(request, "visa/inicio.html")



def logout_view(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('login')
    
    # Puedes redirigir a la página de login o mostrar un mensaje en caso de método GET
    return redirect('login')

