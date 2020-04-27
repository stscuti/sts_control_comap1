from .models import *
from rest_framework import serializers

class SolicitudesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Solicitud143_Step1
		fields = ['num_expediente','estado_solicitud']

class SolicitudesLocalizacionesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Solicitud143_Step1b
		fields = ['num_expediente','direccion']
