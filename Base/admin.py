from django.contrib import admin
from .models import Pais, Departamento, Localidad, Tipo_Documento, Ministerios


# Register your models here.

admin.site.register(Pais)
admin.site.register(Departamento)
admin.site.register(Localidad)
admin.site.register(Tipo_Documento)
admin.site.register(Ministerios)