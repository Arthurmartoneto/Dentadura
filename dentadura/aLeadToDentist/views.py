from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import logout

from .forms import ProfilePictureForm  # Importa o form
from .models import UserProfile

# Decorator para verificar se o usuário pertence ao grupo 'Dashboard'
def in_dashboard_group(user):
    return user.groups.filter(name='Dashboard').exists()

# Acesso base.html
def home(request):
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email  # Obtém o email do usuário
        context = {
            'username': username,
            'email': email
        }
    else:
        return redirect('login')  # Redireciona para a página de login se não estiver autenticado
    return render(request, 'base.html', context)

#
@login_required
@user_passes_test(in_dashboard_group)
def dashboard(request):
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email  # Obtém o email do usuário
        context = {
            'username': username,
            'email': email
        }
    return render(request, 'dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Redireciona para a página inicial após o login
            return redirect('dashboard')
        else:
            error_message = 'Usuário ou senha incorretos. Tente novamente.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def upload_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile picture updated successfully.')
            return redirect('index')  # Redireciona para a página inicial ou outra página desejada após o sucesso
        else:
            messages.error(request, 'Failed to update profile picture. Please check the form.')
    else:
        try:
            form = ProfilePictureForm(instance=request.user.userprofile)
        except UserProfile.DoesNotExist:
            messages.error(request, 'User profile does not exist.')
            return redirect('index')  # Redireciona para a página inicial ou outra página desejada após o erro

    return render(request, 'upload_profile_picture.html', {'form': form})
