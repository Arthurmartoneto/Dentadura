from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth import logout

from .forms import FuncionarioForm, CreateFuncionario
from .models import Funcionario

def in_gerencia_group(user):
    return user.groups.filter(name='Gerencia').exists()


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
            return redirect('profile')
        else:
            error_message = 'Usuário ou senha incorretos. Tente novamente.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


@login_required
def home(request):
    user = request.user
    
    # Verifica se o usuário está no grupo 'Gerencia'
    in_gerencia = user.groups.filter(name='Gerencia').exists()
    
    try:
        funcionario = Funcionario.objects.get(usuario=user)
    except Funcionario.DoesNotExist:
        funcionario = None
    
    context = {
        'in_gerencia': in_gerencia,
        'nome': funcionario.nome if funcionario else '',
        'sobrenome': funcionario.sobrenome if funcionario else '',
    }
    
    return render(request, 'base.html', context)



@login_required
@user_passes_test(in_gerencia_group)
def dashboard(request):
    user = request.user
    
    # Verifica se o usuário está no grupo 'Gerencia'
    in_gerencia = user.groups.filter(name='Gerencia').exists()
    
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email  # Obtém o email do usuário
        context = {
            'username': username,
            'email': email,
            'in_gerencia': in_gerencia,
        }
    return render(request, 'navbar/dashboard.html', context)


@login_required
def profile(request):
    user = request.user
    
    # Verifica se o usuário está no grupo 'Gerencia'
    in_gerencia = user.groups.filter(name='Gerencia').exists()
    
    
    try:
        funcionario = Funcionario.objects.get(usuario=user)
    except Funcionario.DoesNotExist:
        funcionario = None

    if request.method == 'POST':
        form = FuncionarioForm(request.POST, request.FILES, instance=funcionario)
        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.usuario = user
            funcionario.save()
            messages.success(request, "Informações atualizadas com sucesso.")
            return redirect('profile')
        else:
            messages.error(request, "Corrija os erros abaixo.")
    else:
        form = FuncionarioForm(instance=funcionario)

    context = {
        'form': form,
        'username': user.username,
        'email': user.email,
        'funcionario': funcionario,
        'request_user': user,  # Adicionando a referência ao usuário
        'in_gerencia': in_gerencia,
    }
    return render(request, 'profile/profile.html', context)


@login_required
def view_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
        
    # Verifica se o usuário está no grupo 'Gerencia'
    in_gerencia = user.groups.filter(name='Gerencia').exists()
    
    try:
        funcionario = Funcionario.objects.get(usuario=user)
    except Funcionario.DoesNotExist:
        funcionario = None

    context = {
        'user': user,
        'username': user.username,
        'email': user.email,
        'funcionario': funcionario,
        'in_gerencia': in_gerencia,
    }

    return render(request, 'profile/view_profile.html', context)



@login_required
def agendamentos(request):
    user = request.user
    
    # Verifica se o usuário está no grupo 'Gerencia'
    in_gerencia = user.groups.filter(name='Gerencia').exists()
    
    context = {}  # Initialize context
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email  # Get the user's email
        context = {
            'username': username,
            'email': email,
            'in_gerencia': in_gerencia,
        }
        
    return render(request, 'navbar/agendamentos.html', context)

@login_required
def pacientes(request):
    user = request.user
    
    # Verifica se o usuário está no grupo 'Gerencia'
    in_gerencia = user.groups.filter(name='Gerencia').exists()
    
    context = {}  # Initialize context
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email  # Get the user's email
        context = {
            'username': username,
            'email': email,
            'in_gerencia': in_gerencia,
        }
        
    return render(request, 'navbar/pacientes.html', context)


from django.contrib.auth.models import Group

@login_required
@user_passes_test(in_gerencia_group)
def funcionarios(request):
    user = request.user
    
    # Verifica se o usuário está no grupo 'Gerencia'
    in_gerencia = user.groups.filter(name='Gerencia').exists()
    
    # Buscar todos os funcionários
    funcionarios = Funcionario.objects.all()
    
    # Obter informações do usuário autenticado
    username = user.username
    email = user.email
    
    # Inicializar o formulário
    form = CreateFuncionario()

    if request.method == 'POST':
        form = CreateFuncionario(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Adiciona o novo usuário ao grupo "Funcionários"
            funcionarios_group = Group.objects.get(name='Funcionarios')
            user.groups.add(funcionarios_group)
            
            # Cria um novo registro de Funcionario
            Funcionario.objects.create(usuario=user)
            
            messages.success(request, "Funcionário criado com sucesso!")
            return redirect('funcionarios')  # Redireciona para a mesma página para atualizar a lista
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    
    context = {
        'funcionarios': funcionarios,
        'username': username,
        'email': email,
        'form': form,
        'in_gerencia': in_gerencia,
    }
    
    return render(request, 'navbar/funcionarios.html', context)




# ESTOQUE #########################################
@login_required
def produtos(request):
    user = request.user
    
    # Verifica se o usuário está no grupo 'Gerencia'
    in_gerencia = user.groups.filter(name='Gerencia').exists()
    
    context = {}  # Initialize context
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email  # Get the user's email
        context = {
            'username': username,
            'email': email,
            'in_gerencia': in_gerencia,
        }
        
    return render(request, 'estoque/produtos.html', context)

@login_required
def equipamentos(request):
    user = request.user
    
    # Verifica se o usuário está no grupo 'Gerencia'
    in_gerencia = user.groups.filter(name='Gerencia').exists()
    
    context = {}  # Initialize context
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email  # Get the user's email
        context = {
            'username': username,
            'email': email,
            'in_gerencia': in_gerencia,
        }
        
    return render(request, 'estoque/equipamentos.html', context)