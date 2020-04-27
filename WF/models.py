from django.db import models
from Usuarios.models import Usuario
# Create your models here.

class ModeloBaseRegistro(models.Model):
	estado = models.BooleanField(default=True)
	fc = models.DateTimeField(auto_now_add=True)
	fm = models.DateTimeField(auto_now=True)
	uc = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	um = models.BigIntegerField(blank=True, null=True)

	class Meta:
		abstract = True
