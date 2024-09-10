from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('inicio', views.inicio, name='inicio'),
    path('login', views.login_view, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]