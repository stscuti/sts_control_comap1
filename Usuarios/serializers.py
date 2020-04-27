from .models import *
from rest_framework import serializers

class UsuariosSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Usuario
		fields = ['identificador','password','correo','direccion','telefono','celular','tipo_usuario','active','staff','admin','solicitante','ventanilla_unica','coordinador_ventanilla_unica','evaluador','evaluador_sectorial','coordinador_evaluador_sectorial','aprobador_sectorial','coordinador_aprobador_sectorial','evaluador_comap','control_contable','coordinador_control_contable','control_obra_civil','coordinador_control_obra_civil','control_juridico','responsable_mef','responsable_miem','responsable_mgap','responsable_mintur','responsable_mtss','coordinacion','coordinacion_general','ministerio_mef','ministerio_miem','ministerio_mgap','ministerio_mintur','ministerio_mtss']

