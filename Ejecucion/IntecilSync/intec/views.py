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

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirige a la página deseada después del login
        else:
            error_message = "Credenciales no válidas. Por favor, inténtalo de nuevo."
            request.session['error_message'] = error_message
            return redirect('login')
        

    error_message = request.session.pop('error_message', None)
    return render(request, 'users/login.html', {'error_message': error_message})


def logout_view(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('login')
    
    # Puedes redirigir a la página de login o mostrar un mensaje en caso de método GET
    return redirect('login')

