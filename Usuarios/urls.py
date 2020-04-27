from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from Control_Coordinacion import views as Vistas_Control_Coordinacion
from Control_Seguimiento_Contable import views as Vistas_Control_Seguimiento_Contable
from Control_Seguimiento_Obra import views as Vistas_Control_Seguimiento_Obra
from Control_VU import views as Vistas_Control_VU
from Evaluacion import views as Vistas_Evaluacion
from Usuarios import views as Vistas_Usuarios
from Contribuyentes import views as Vistas_Contribuyentes
from Solicitudes import views as Vistas_Solicitudes
from Mensajeria import views as Vistas_Mensajeria
from COMAP_Control import views as Vistas_COMAP_Control
from WS import views as Vistas_WS
from WF import views as Vistas_WF 


urlpatterns = [
	
    path('', Vistas_COMAP_Control.Home.as_view(), name='MiInicio'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='Logout'),
    path('registro_contribuyente/', Vistas_Usuarios.MultiContribuyenteCreateView.as_view(template_name='registrocontribuyente.html'), name='Registro_Contribuyente'),
    path('contribuyente_grabado/', Vistas_Usuarios.ContribuyenteSuccessView.as_view(template_name='contribuyentegrabado.html'), name='Contribuyente_Grabado'),
    path('registro_personafisica/', Vistas_Usuarios.MultiPersonaFisicaCreateView.as_view(template_name='registropersonafisica.html'), name='Registro_PersonaFisica'),
    path('personafisica_grabado/', Vistas_Usuarios.PersonaFisicaSuccessView.as_view(template_name='personafisicagrabado.html'), name='PersonaFisica_Grabado'),
    #path('activate/<slug:uidb64>/<slug:token>/', Vistas_Usuarios.Activate.as_view(), name='activate'),
    #path('activate/(?P<uidb64>[-a-zA-Z0-9_]+)/(?P<token>[-a-zA-Z0-9_]+)/$', Vistas_Usuarios.Activate.as_view(), name='activate'),
    path('activate/<slug:uidb64>/<slug:token>/<slug:key>/', Vistas_Usuarios.Activate.as_view(), name='activate'),
    re_path('activate/(?P<uidb64>[-a-zA-Z0-9_]+)/(?P<token>[-a-zA-Z0-9_]+)/(?P<key>[-a-zA-Z0-9_]+)/$', Vistas_Usuarios.Activate.as_view(), name='activate2'),
    #path('cotizaciones/', Vistas_WS.CotizacionesCreateView.as_view(template_name='cotizaciones.html'), name='Cotizaciones'),

    path('api/usuarios/', Vistas_Usuarios.UsuarioList.as_view(), name='Usuarios'),


]