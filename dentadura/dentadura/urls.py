"""dentadura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aLeadToDentist import views as core_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', core_views.home, name='home'),
    
    path('', core_views.dashboard, name='dashboard'),
    path('profile/', core_views.profile, name='profile'),
    path('profile/<str:user_id>/', core_views.view_profile, name='user_profile'),
    
    path('login/', core_views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('produtos/', core_views.produtos, name='produtos'),
    path('equipamentos/', core_views.equipamentos, name='equipamentos'),

    path('agendamentos/', core_views.agendamentos, name='agendamentos'),
    path('pacientes/', core_views.pacientes, name='pacientes'),
    path('funcionarios/', core_views.funcionarios, name='funcionarios'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
