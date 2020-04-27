"""COMAP_Control URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Control_Coordinacion import views
from Control_Seguimiento_Contable import views
from Control_Seguimiento_Obra import views
from Control_VU import views
from Evaluacion import views
from Usuarios import views
from Contribuyentes import views
from Solicitudes import views
from Mensajeria import views
from COMAP_Control import views
from WS import views
from WF import views
from Base import views
from rest_framework.authtoken import views

urlpatterns = [
	path('', include(('Usuarios.urls','Usuarios'), namespace='Usuarios')),
	path('', include(('WS.urls','WS'), namespace='WS')),
	
	path('', include(('Base.urls','Base'), namespace='Base')),
	path('', include(('Contribuyentes.urls','Contribuyentes'), namespace='Contribuyentes')),
    path('', include(('Solicitudes.urls','Solicitudes'), namespace='Solicitudes')),
    path('api/v1/auth', include(('rest_framework.urls','rest_framework'), namespace='rest_framework')),
	path('admin/', admin.site.urls),

]
