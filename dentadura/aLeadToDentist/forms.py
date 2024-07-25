from django import forms
from .models import Funcionario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            'id_funcionario', 'nome', 'sobrenome', 'data_nascimento', 'genero', 'email',
            'telefone', 'endereco', 'cidade', 'estado', 'cep', 'pais', 'cargo', 
            'departamento', 'data_admissao', 'salario', 'status_emprego', 'foto_perfil'
        ]
        widgets = {
            'id_funcionario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Matrícula'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nome'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Sobrenome'}),
            'data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'genero': forms.RadioSelect(choices=[('M', 'Masculino'), ('F', 'Feminino')]),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Telefone'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Endereço'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Cidade'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Estado'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter CEP'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter País'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Cargo'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Departamento'}),
            'data_admissao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'salario': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Salário'}),
            'status_emprego': forms.Select(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo'), ('Temporário', 'Temporário')], attrs={'class': 'form-control'}),
        }
        

class CreateFuncionario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2