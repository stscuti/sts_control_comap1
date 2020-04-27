from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView
from .forms import MultiContribuyenteModelForm, MultiPersonaFisicaModelForm, FormUsuario, FormContribuyente_sid, FormPersonaFisica_sid, NuevoLinkActivacionModelForm
from .models import Activacion

#Para Email
from django.views import View
from django.http import HttpResponse
#from django.shortcuts import render
#from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
#from django.utils.encoding import force_bytes
#from django.utils.http import urlsafe_base64_encode
from .token import token_activacion_cuenta, generate_activation_key
from django.core.mail import EmailMessage, send_mail
#Vista de Activacion
from django.contrib.auth import get_user_model, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
#from .token import account_activation_token
from django.template.loader import render_to_string
from datetime import datetime, timedelta, tzinfo, time, date
import pytz
from django.utils import timezone

#Para WS
from zeep import Client
from requests import Session
from requests.auth import HTTPBasicAuth

#Para API
from rest_framework import generics
from .models import Usuario
from .serializers import UsuariosSerializer








# Create your views here.

class MultiContribuyenteCreateView(CreateView):
	form_class = MultiContribuyenteModelForm
	template_name = 'registrocontribuyente.html'

	def get(self, request):
		form = MultiContribuyenteModelForm()
		return render(request, 'registrocontribuyente.html', {'form': form})

	def form_valid(self, form):
		# Create an inactive user with no password:
		UsuarioPrincipal = form['UsuarioMain'].save(commit=False)
		UsuarioPrincipal.active = False
		UsuarioPrincipal.set_unusable_password()
		UsuarioPrincipal.save()

		Contribuyente = form['Contribuyente'].save(commit=False)
		Contribuyente.identificador = UsuarioPrincipal
		Contribuyente.save()

		MActivacion = form['Activacion'].save(commit=False)
		MActivacion.identificador = UsuarioPrincipal
		MActivacion.activation_key = generate_activation_key(UsuarioPrincipal.identificador)
		MActivacion.key_expires = datetime.now() + timedelta(days=2)

		MContribuyente = form['ModeloContribuyente'].save(commit=False)
		MContribuyente.identificador = UsuarioPrincipal

		MContribuyente.save()

		MActivacion.save()
		#Enviar correo y token
		mail_subject = 'Activa tu Cuenta'
		current_site = get_current_site(self.request)
		uid = urlsafe_base64_encode(force_bytes(UsuarioPrincipal.pk))
		token = token_activacion_cuenta.make_token(UsuarioPrincipal)
		#activation_link = "{0}/?uid={1}&token{2}".format(current_site, uid, token)
		#message = "Hello {0},\n {1}".format(UsuarioPrincipal.identificador, activation_link)
		message = render_to_string('mail_activacion.html', {
				'user': UsuarioPrincipal.identificador,
				'domain': current_site,
				'uid': urlsafe_base64_encode(force_bytes(UsuarioPrincipal.pk)),
				'token': token,
				'activation_key': MActivacion.activation_key,
				'key_expires': MActivacion.key_expires,
			})
		to_email = form['UsuarioMain'].cleaned_data.get('correo')
		email = EmailMessage(mail_subject, message, to=[to_email])
		email.send()
		miemail = EmailMessage("Hola Contribuyente", "Como estas", to=["federico.bentos@yahoo.com"])
		miemail.send()
		return HttpResponseRedirect(reverse('Usuarios:Contribuyente_Grabado'))


class ContribuyenteSuccessView(TemplateView):
    template_name = 'contribuyentegrabado.html'

'''
class MultiPersonaFisicaCreateView(CreateView):
    form_class = MultiPersonaFisicaModelForm
    template_name = 'registropersonafisica.html'

    def form_valid(self, form):
        #UsuarioPrincipal.password = form['UsuarioMain'].password1
        UsuarioPrincipal = form['UsuarioMain'].save()
        PersonaFisica = form['PersonaFisica'].save(commit=False)
        
        PersonaFisica.identificador = UsuarioPrincipal
        PersonaFisica.save()
        return HttpResponseRedirect(reverse('Usuarios:PersonaFisica_Grabado'))
'''
class PersonaFisicaSuccessView(TemplateView):
    template_name = 'personafisicagrabado.html'



class MultiPersonaFisicaCreateView(CreateView):
    form_class = MultiPersonaFisicaModelForm
    template_name = 'registropersonafisica.html'

    def get(self, request):
        form = MultiPersonaFisicaModelForm()
        return render(request, 'registropersonafisica.html', {'form': form})


    def form_valid(self, form):
    	# Create an inactive user with no password:
    	UsuarioPrincipal = form['UsuarioMain'].save(commit=False)
    	UsuarioPrincipal.active = False
    	UsuarioPrincipal.set_unusable_password()
    	UsuarioPrincipal.save()

    	PersonaFisica = form['PersonaFisica'].save(commit=False)
    	PersonaFisica.identificador = UsuarioPrincipal
    	PersonaFisica.save()

    	MActivacion = form['Activacion'].save(commit=False)
    	MActivacion.identificador = UsuarioPrincipal
    	MActivacion.activation_key = generate_activation_key(UsuarioPrincipal.identificador)
    	MActivacion.key_expires = datetime.now() + timedelta(days=2)

    	MActivacion.save()
    	#Enviar correo y token
    	mail_subject = 'Activa tu Cuenta'
    	current_site = get_current_site(self.request)
    	uid = urlsafe_base64_encode(force_bytes(UsuarioPrincipal.pk))
    	token = token_activacion_cuenta.make_token(UsuarioPrincipal)
    	#activation_link = "{0}/?uid={1}&token{2}".format(current_site, uid, token)
    	#message = "Hello {0},\n {1}".format(UsuarioPrincipal.identificador, activation_link)
    	message = render_to_string('mail_activacion.html', {
                'user': UsuarioPrincipal.identificador,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(UsuarioPrincipal.pk)),
                'token': token,
                'activation_key': MActivacion.activation_key,
                'key_expires': MActivacion.key_expires,
            })
    	to_email = form['UsuarioMain'].cleaned_data.get('correo')
    	email = EmailMessage(mail_subject, message, to=[to_email])
    	email.send()
    	miemail = EmailMessage("Hola Persona Fisica", "Como estas", to=["federico.bentos@yahoo.com"])
    	miemail.send()
    	return HttpResponseRedirect(reverse('Usuarios:PersonaFisica_Grabado'))


User = get_user_model()

class Activate(View):

	def get(self, request, uidb64, token, key):
		objeto_activacion = Activacion.objects.get(activation_key=key)
		try:
			uid = force_text(urlsafe_base64_decode(uidb64))
			user = User.objects.get(pk=uid)
			#objeto_activacion = get_object_or_404(Activacion, activation_key=key)
			#objeto_activacion = Activacion.objects.get(activation_key=key)
			#if request.user.is_authenticated():
				#return redirect('Usuarios:MiInicio')
		except(TypeError, ValueError, OverflowError, User.DoesNotExist):
			user = None
			objeto_activacion = None
		if user is not None:
			if objeto_activacion is not None:
				if user.active == False:
					#utc=pytz.UTC
					#fecha_expiracion=objeto_activacion.key_expires.replace(tzinfo=utc)
					if objeto_activacion.key_expires > timezone.now():
						if objeto_activacion.activation_key == key and token_activacion_cuenta.check_token(user, token):
							# activate user and login:
							user.active = True
							user.save()
							login(request, user)
							form = SetPasswordForm(request.user)
							#form = PasswordChangeForm(request.user)
							return render(request, 'activation.html', {'form': form, 'uidb64': uid, 'token': token, 'key': key})
						else:
							return HttpResponse('Token o Clave incorrecta')
					else:
						return HttpResponse('Key Vencida, solicite una nueva')
				else:
					return HttpResponse('La Cuenta ya esta activada')
			else:
				return HttpResponse('Objeto Activacion no encontrado')
		else:
			return HttpResponse('El Usuario no encontrado!')

	def post(self, request, uidb64, token, key):
		if request.method == "POST":
			User = get_user_model()
			user = User.objects.get(pk=uidb64)
			form = SetPasswordForm(request.user, request.POST)
			#form = PasswordChangeForm(request.user, request.POST)
			if user is None:
				return HttpResponse("Usuario no encontrado")
			if form.is_valid():
				user = form.save()
				update_session_auth_hash(request, user)
				return HttpResponseRedirect(reverse('Usuarios:MiInicio'))
			else:
				#user.active = False
				#user.save()
				mensaje = "Algo fallo: " + "---" + token + "---" + uidb64 + "---" + user.password + "---" + key
				return HttpResponse(mensaje)
		else:
			return HttpResponse('Algo fallo desde el principio')

'''
class Nuevo_Link_Activacion(UpdateView):
	form_class = NuevoLinkActivacionModelForm
	model = Activacion
    template_name = 'nuevolinkactivacion.html'

    def get(self, request):
        form = NuevoLinkActivacionModelForm()
        return render(request, 'nuevolinkactivacion.html', {'form': form})
    def form_valid(self, form):
'''

'''
class Activate(View):
	#success_url = 'Usuarios:MiInicio'
	if request.user.is_authenticated():
        return redirect('Usuarios:MiInicio')
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and token_activacion_cuenta.check_token(user, token):
            # activate user and login:
            user.active = True
            user.save()
            login(request, user)

            form = PasswordChangeForm(request.user)
            return render(request, 'activation.html', {'form': form, 'uidb64': uid, 'token': token})
        else:
            return HttpResponse('Activation link is invalid!')
    def post(self, request, uidb64, token):
    	if request.method == "POST":
    		User = get_user_model()
    		user = User.objects.get(pk=uidb64)
    		
    		form = PasswordChangeForm(request.user, request.POST)
    		if user is None:
    			return HttpResponse("Usuario es None")
    		if form.is_valid():
    			user = form.save()
    			update_session_auth_hash(request, user)
    			#return render(request, 'index.html', {'form':form, 'uidb64':uidb64, 'token':token})
    			return HttpResponseRedirect(reverse('Usuarios:MiInicio'))
    		else:
    			user.active = False
    			user.save()
    			mensaje = "Algo fallo: " + "---" + token + "---" + uidb64 + "---" + user.password
    			return HttpResponse(mensaje)
    	else:
    		return HttpResponse('Algo fallo desde el principio')
'''




'''
    def post(self, request, uidb64, token):
    	try:
    		uid = force_text(urlsafe_base64_decode(uidb64))
    		user = User.objects.get(pk=uid)
    		if request.method == 'POST':
    			form = PasswordChangeForm(request.user, request.POST, uidb64, token)
    			if form.is_valid():
    				user = form.save()
    				update_session_auth_hash(request, user) # Important, to update the session with the new password
    				#return HttpResponse(reverse('Usuarios:MiInicio'))
    				return render(request, 'Usuarios:MiInicio', {'form': form, 'uidb64': uid, 'token': token})
    			else:
    				mensaje = "Algo fallo: "  + "---" + uidb64 + "---" + token + "---" + user.password
    				return HttpResponse(mensaje)
    		else:
    			return HttpResponse('Algo fallo desde el principio')
    	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
    		return HttpResponse('No se puede activar')
    		'''

class UsuarioList(generics.ListCreateAPIView):
	queryset = Usuario.objects.all()
	serializer_class = UsuariosSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk = self.kwargs['pk'],
		)
		return obj

