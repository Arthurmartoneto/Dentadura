# urls.py

from django.urls import path
from django.contrib.auth import views as auth_views  # Para usar views padrão do Django
from . import views  # Suas views personalizadas

urlpatterns = [
    # Páginas de autenticação
    path('', views.login_view, name='login'),  # Certifique-se de que `login_view` está definido corretamente
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Usando a view padrão de logout
    
    # Páginas principais
    path('base/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    
    # Outras seções
    path('produtos/', views.produtos, name='produtos'),
    path('equipamentos/', views.equipamentos, name='equipamentos'),
    
    path('agendamentos/', views.agendamentos, name='agendamentos'),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('funcionarios/', views.funcionarios, name='funcionarios'),
        
]
