from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.



def dashboard(request):
    return render(request, 'dashboard.html')


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
    logout(request)
    return redirect('login')  # Redirige a la página de login después del logout


def inicio(request):
    return render(request, "visa/inicio.html")