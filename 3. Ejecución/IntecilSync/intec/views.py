from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
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



def admin_view(request):

    if request.method == 'GET':
        return render(request, 'admin/admin_view.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:

            try:
                print (request.POST)
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('admin_view')

            except IntegrityError:
                return render(request, 'admin/admin_view.html', {
                'form': UserCreationForm,
                'error': 'User already exists'
                })

        return render(request, 'admin/admin_view.html', {
                 'form': UserCreationForm,
                 'error': 'Password no not match'
                })