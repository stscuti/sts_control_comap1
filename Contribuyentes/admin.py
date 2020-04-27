from django.contrib import admin
from .models import Contribuyente, Domicilio_Fiscal, Domicilio_Constituido, Propietarios, Representantes, Directores

# Register your models here.

admin.site.register(Contribuyente)
admin.site.register(Domicilio_Fiscal)
admin.site.register(Domicilio_Constituido)
admin.site.register(Propietarios)
admin.site.register(Representantes)
admin.site.register(Directores)