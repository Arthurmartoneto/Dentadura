from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import logout

from .forms import FuncionarioForm
from .models import Funcionario

# Decorator para verificar se o usuário pertence ao grupo 'Dashboard'
def in_dashboard_group(user):
    return user.groups.filter(name='Dashboard').exists()


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


@login_required
def home(request):
    user = request.user
    try:
        funcionario = Funcionario.objects.get(usuario=user)
    except Funcionario.DoesNotExist:
        funcionario = None
    

    context = {
        'nome': funcionario.nome if funcionario else '',
        'sobrenome': funcionario.sobrenome if funcionario else '',
    }
    
    return render(request, 'base.html', context)



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


@login_required
def profile(request):
    user = request.user
    try:
        funcionario = Funcionario.objects.get(usuario=user)
    except Funcionario.DoesNotExist:
        funcionario = None
    
    if request.method == 'POST':
        if funcionario:
            form = FuncionarioForm(request.POST, request.FILES, instance=funcionario)
        else:
            form = FuncionarioForm(request.POST, request.FILES)
        
        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.usuario = user
            funcionario.save()
            messages.success(request, "Informações atualizadas com sucesso.")
            return redirect('profile')
    else:
        form = FuncionarioForm(instance=funcionario)
    
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email  # Obtém o email do usuário
    
    context = {
        'form': form,
        'username': username,
        'email': email,
        'nome': funcionario.nome if funcionario else '',
        'sobrenome': funcionario.sobrenome if funcionario else '',
    }
    return render(request, 'profile.html', context)



@login_required
def agendamentos(request):
    context = {}  # Initialize context
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email  # Get the user's email
        context = {
            'username': username,
            'email': email
        }
    return render(request, 'agendamentos.html', context)

@login_required
def pacientes(request):
    context = {}  # Initialize context
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email  # Get the user's email
        context = {
            'username': username,
            'email': email
        }
    return render(request, 'pacientes.html', context)


@login_required
def funcionarios(request):
    user = request.user
    funcionario = Funcionario.objects.filter(usuario=user).first()

    if request.method == 'POST':
        if funcionario:
            form = FuncionarioForm(request.POST, request.FILES, instance=funcionario)
        else:
            form = FuncionarioForm(request.POST, request.FILES)
        
        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.usuario = user  # Associa o funcionário ao usuário logado
            funcionario.save()
            return redirect('funcionarios')  # Redireciona para a mesma página após salvar
    else:
        form = FuncionarioForm(instance=funcionario)

    context = {
        'username': user.username,
        'email': user.email,
        'form': form,
        'funcionario': funcionario
    }
    return render(request, 'funcionarios.html', context)



# ESTOQUE #########################################
@login_required
def produtos(request):
    context = {}  # Initialize context
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email  # Get the user's email
        context = {
            'username': username,
            'email': email
        }
    return render(request, 'produtos.html', context)

@login_required
def equipamentos(request):
    context = {}  # Initialize context
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email  # Get the user's email
        context = {
            'username': username,
            'email': email
        }
    return render(request, 'equipamentos.html', context)