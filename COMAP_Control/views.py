from django.conf import settings
from django.contrib import auth, messages
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.views import generic






class Home(LoginRequiredMixin, View):
	#LoginRequiredMixin,

	#login_url = self.request.build_absolute_uri('/')[:-1].strip("/")
	login_url = 'Usuarios:Login'
	def get(self, request, *args, **kwargs):
		if "iud" in request.build_absolute_uri('/')[:-1].strip("/"):
			login_url = request.build_absolute_uri('/')[:-1].strip("/")
		else:
			login_url = 'Usuarios:Login'
		return render(request, 'index.html')
	
	def absolute(request):
	    urls = {
	        'ABSOLUTE_ROOT': request.build_absolute_uri('/')[:-1].strip("/"),
	        'ABSOLUTE_ROOT_URL': request.build_absolute_uri('/').strip("/"),
	    }
	    return urls
	
	