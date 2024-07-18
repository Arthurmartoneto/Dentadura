from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('base/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    
    path('upload_profile_picture/', views.upload_profile_picture, name='upload_profile_picture'),
]