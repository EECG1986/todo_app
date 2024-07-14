"""
URL configuration for todo_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el panel de administración de Django
    path('', views.index, name='index'),  # Página de inicio, renderizada por la vista 'index' de la app 'tasks'
    path('tasks/', include('tasks.urls')),  # Incluye las URLs definidas en 'tasks.urls'
    path('signup/', views.signup, name='signup'),  # URL para registrarse, renderizada por la vista 'signup' de 'tasks.views'
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # URL para iniciar sesión
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),  # URL para cerrar sesión
]
