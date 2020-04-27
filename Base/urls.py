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
from Base import views as Vistas_Base 


urlpatterns = [
	
	path('template_paises_departamentos_localidades/', Vistas_Base.Paises_Departamentos_Localidades_TemplateView.as_view(template_name='template_paises_departamentos_localidades.html'), name='Template_Paises_Departamentos_Localidades'),
	path('listado_paises/', Vistas_Base.ListadoPaises.as_view(template_name='paises.html'), name='Listado_Paises'),
	path('crear_paises/', Vistas_Base.CrearPais.as_view(template_name='crear_pais.html'), name='Crear_Pais'),
	path('actualizar_paises/', Vistas_Base.ActualizarPais.as_view(template_name='actualizar_pais.html'), name='Actualizar_Pais'),
	path('crear_paises_individual/', Vistas_Base.Paises_CreateView.as_view(template_name='crear_pais_individual.html'), name='Crear_Pais_Individual'),
	path('actualizar_paises_individual/<int:pk>', Vistas_Base.Paises_UpdateView.as_view(template_name='actualizar_pais_individual.html'), name='Actualizar_Pais_Individual'),	
	path('eliminar_paises_individual/<int:pk>', Vistas_Base.Paises_DeleteView.as_view(template_name='eliminar_pais_individual.html'), name='Eliminar_Pais_Individual'),
	path('detalles_paises_individual/<int:pk>', Vistas_Base.Paises_DetailView.as_view(template_name='detalle_pais_individual.html'), name='Detalle_Pais_Individual'),
	
	path('listado_departamentos/', Vistas_Base.ListadoDepartamentos.as_view(template_name='departamentos.html'), name='Listado_Departamentos'),
	path('crear_departamentos_individual/', Vistas_Base.Departamentos_CreateView.as_view(template_name='crear_departamento_individual.html'), name='Crear_Departamento_Individual'),
	path('actualizar_departamentos_individual/<int:pk>', Vistas_Base.Departamentos_UpdateView.as_view(template_name='actualizar_departamento_individual.html'), name='Actualizar_Departamento_Individual'),	
	path('eliminar_departamentos_individual/<int:pk>', Vistas_Base.Departamentos_DeleteView.as_view(template_name='eliminar_departamento_individual.html'), name='Eliminar_Departamento_Individual'),
	path('detalles_departamentos_individual/<int:pk>', Vistas_Base.Departamentos_DetailView.as_view(template_name='detalle_departamento_individual.html'), name='Detalle_Departamento_Individual'),
	
	path('listado_localidades/', Vistas_Base.ListadoLocalidades.as_view(template_name='localidades.html'), name='Listado_Localidades'),
	path('crear_localidades_individual/', Vistas_Base.Localidades_CreateView.as_view(template_name='crear_localidad_individual.html'), name='Crear_Localidad_Individual'),
	path('actualizar_localidades_individual/<int:pk>', Vistas_Base.Localidades_UpdateView.as_view(template_name='actualizar_localidad_individual.html'), name='Actualizar_Localidad_Individual'),	
	path('eliminar_localidades_individual/<int:pk>', Vistas_Base.Localidades_DeleteView.as_view(template_name='eliminar_localidad_individual.html'), name='Eliminar_Localidad_Individual'),
	path('detalles_localidades_individual/<int:pk>', Vistas_Base.Localidades_DetailView.as_view(template_name='detalle_localidad_individual.html'), name='Detalle_Localidad_Individual'),
	
	path('listado_tipodocumento/', Vistas_Base.ListadoTipoDocumento.as_view(template_name='listado_tipo_documento.html'), name='Listado_Tipo_Documento'),
	path('crear_tipodocumento/', Vistas_Base.TipoDocumento_CreateView.as_view(template_name='crear_tipo_documento.html'), name='Crear_Tipo_Documento'),
	path('actualizar_tipodocumento/<int:pk>', Vistas_Base.TipoDocumento_UpdateView.as_view(template_name='actualizar_tipo_documento.html'), name='Actualizar_Tipo_Documento'),	
	path('eliminar_tipodocumento/<int:pk>', Vistas_Base.TipoDocumento_DeleteView.as_view(template_name='eliminar_tipo_documento.html'), name='Eliminar_Tipo_Documento'),
	path('detalles_tipodocumento/<int:pk>', Vistas_Base.TipoDocumento_DetailView.as_view(template_name='detalle_tipo_documento.html'), name='Detalle_Tipo_Documento'),

	path('template_categorias_subcategorias/', Vistas_Base.Categoria_SubCategoria_Inversiones_TemplateView.as_view(template_name='template_categorias_subcategorias.html'), name='Listado_Categoria_SubCategoria_Inversiones'),
	path('listado_categorias/', Vistas_Base.ListadoCategoriaInversiones.as_view(template_name='listado_categoria_inversiones.html'), name='Listado_Categorias'),
	path('crear_categorias_individual/', Vistas_Base.Categoria_Inversiones_CreateView.as_view(template_name='crear_categoria_inversiones.html'), name='Crear_Categoria_Inversion_Individual'),
	path('actualizar_categorias_individual/<int:pk>', Vistas_Base.Categoria_Inversiones_UpdateView.as_view(template_name='actualizar_categoria_inversiones.html'), name='Actualizar_Categoria_Inversion_Individual'),	
	path('eliminar_categorias_individual/<int:pk>', Vistas_Base.Categoria_Inversiones_DeleteView.as_view(template_name='eliminar_categoria_inversiones.html'), name='Eliminar_Categoria_Inversion_Individual'),
	path('detalles_categorias_individual/<int:pk>', Vistas_Base.Categoria_Inversiones_DetailView.as_view(template_name='detalle_categoria_inversiones.html'), name='Detalle_Categoria_Inversion_Individual'),

	path('listado_subcategorias/', Vistas_Base.ListadoSubCategoriaInversiones.as_view(template_name='listado_subcategoria_inversiones.html'), name='Listado_SubCategorias'),
	path('crear_subcategorias_individual/', Vistas_Base.SubCategoria_Inversiones_CreateView.as_view(template_name='crear_subcategoria_inversiones.html'), name='Crear_SubCategoria_Inversion_Individual'),
	path('actualizar_subcategorias_individual/<int:pk>', Vistas_Base.SubCategoria_Inversiones_UpdateView.as_view(template_name='actualizar_subcategoria_inversiones.html'), name='Actualizar_SubCategoria_Inversion_Individual'),	
	path('eliminar_subcategorias_individual/<int:pk>', Vistas_Base.SubCategoria_Inversiones_DeleteView.as_view(template_name='eliminar_subcategoria_inversiones.html'), name='Eliminar_SubCategoria_Inversion_Individual'),
	path('detalles_subcategorias_individual/<int:pk>', Vistas_Base.SubCategoria_Inversiones_DetailView.as_view(template_name='detalle_subcategoria_inversiones.html'), name='Detalle_SubCategoria_Inversion_Individual'),
	
	path('listado_tipocontribuyente/', Vistas_Base.ListadoTipoContribuyente.as_view(template_name='listado_tipo_contribuyente.html'), name='Listado_Tipo_Contribuyente'),
	path('crear_tipocontribuyente/', Vistas_Base.Tipo_Contribuyente_CreateView.as_view(template_name='crear_tipo_contribuyente.html'), name='Crear_Tipo_Contribuyente'),
	path('actualizar_tipocontribuyente/<int:pk>', Vistas_Base.Tipo_Contribuyente_UpdateView.as_view(template_name='actualizar_tipo_contribuyente.html'), name='Actualizar_Tipo_Contribuyente'),	
	path('eliminar_tipocontribuyente/<int:pk>', Vistas_Base.Tipo_Contribuyente_DeleteView.as_view(template_name='eliminar_tipo_contribuyente.html'), name='Eliminar_Tipo_Contribuyente'),
	path('detalles_tipocontribuyente/<int:pk>', Vistas_Base.Tipo_Contribuyente_DetailView.as_view(template_name='detalle_tipo_contribuyente.html'), name='Detalle_Tipo_Contribuyente'),

	path('listado_ministerios/', Vistas_Base.ListadoMinisterios.as_view(template_name='listado_ministerios.html'), name='Listado_Ministerios'),
	path('crear_ministerio/', Vistas_Base.Ministerios_CreateView.as_view(template_name='crear_ministerio.html'), name='Crear_Ministerio'),
	path('actualizar_ministerio/<int:pk>', Vistas_Base.Ministerios_UpdateView.as_view(template_name='actualizar_ministerio.html'), name='Actualizar_Ministerio'),	
	path('eliminar_ministerio/<int:pk>', Vistas_Base.Ministerios_DeleteView.as_view(template_name='eliminar_ministerio.html'), name='Eliminar_Ministerio'),
	path('detalles_ministerio/<int:pk>', Vistas_Base.Ministerios_DetailView.as_view(template_name='detalle_ministerio.html'), name='Detalle_Ministerio'),

	path('template_tipogiro_girociiu/', Vistas_Base.TipoGiro_GiroCIIU_TemplateView.as_view(template_name='template_tipogiro_girociiu.html'), name='Listado_TipoGiro_GiroCIIU'),
	path('listado_tipogiro/', Vistas_Base.ListadoTipoGiro.as_view(template_name='listado_tipo_giro.html'), name='Listado_TipoGiro'),
	path('crear_tipogiro_individual/', Vistas_Base.TipoGiro_CreateView.as_view(template_name='crear_tipo_giro.html'), name='Crear_Tipo_Giro_Individual'),
	path('actualizar_tipogiro_individual/<int:pk>', Vistas_Base.TipoGiro_UpdateView.as_view(template_name='actualizar_tipo_giro.html'), name='Actualizar_Tipo_Giro_Individual'),	
	path('eliminar_tipogiro_individual/<int:pk>', Vistas_Base.TipoGiro_DeleteView.as_view(template_name='eliminar_tipo_giro.html'), name='Eliminar_Tipo_Giro_Individual'),
	path('detalles_tipogiro_individual/<int:pk>', Vistas_Base.TipoGiro_DetailView.as_view(template_name='detalle_tipo_giro.html'), name='Detalle_Tipo_Giro_Individual'),

	path('listado_girociiu/', Vistas_Base.ListadoGiroCIIU.as_view(template_name='listado_giro_ciiu.html'), name='Listado_Giro_CIIU'),
	path('crear_girociiu_individual/', Vistas_Base.Giro_CIIU_CreateView.as_view(template_name='crear_giro_ciiu.html'), name='Crear_Giro_CIIU_Individual'),
	path('actualizar_girociiu_individual/<int:pk>', Vistas_Base.Giro_CIIU_UpdateView.as_view(template_name='actualizar_giro_ciiu.html'), name='Actualizar_Giro_CIIU_Individual'),	
	path('eliminar_girociiu_individual/<int:pk>', Vistas_Base.Giro_CIIU_DeleteView.as_view(template_name='eliminar_giro_ciiu.html'), name='Eliminar_Giro_CIIU_Individual'),
	path('detalles_girociiu_individual/<int:pk>', Vistas_Base.Giro_CIIU_DetailView.as_view(template_name='detalle_giro_ciiu.html'), name='Detalle_Giro_CIIU_Individual'),

	path('listado_fechabalance/', Vistas_Base.ListadoFechaBalance.as_view(template_name='listado_fecha_balance.html'), name='Listado_Fecha_Balance'),
	path('crear_fechabalance/', Vistas_Base.Fecha_Balance_CreateView.as_view(template_name='crear_fecha_balance.html'), name='Crear_Fecha_Balance'),
	path('actualizar_fechabalance/<int:pk>', Vistas_Base.Fecha_Balance_UpdateView.as_view(template_name='actualizar_fecha_balance.html'), name='Actualizar_Fecha_Balance'),	
	path('eliminar_fechabalance/<int:pk>', Vistas_Base.Fecha_Balance_DeleteView.as_view(template_name='eliminar_fecha_balance.html'), name='Eliminar_Fecha_Balance'),
	path('detalles_fechabalance/<int:pk>', Vistas_Base.Fecha_Balance_DetailView.as_view(template_name='detalle_fecha_balance.html'), name='Detalle_Fecha_Balance'),

	path('listado_localizacion_operaciones/', Vistas_Base.ListadoLocalizacionOperaciones.as_view(template_name='listado_localizacion_operaciones.html'), name='Listado_Localizacion_Operaciones'),
	path('crear_localizacion_operaciones/', Vistas_Base.LocalizacionOperaciones_CreateView.as_view(template_name='crear_localizacion_operaciones.html'), name='Crear_Localizacion_Operaciones'),
	path('actualizar_localizacion_operaciones/<int:pk>', Vistas_Base.LocalizacionOperaciones_UpdateView.as_view(template_name='actualizar_localizacion_operaciones.html'), name='Actualizar_Localizacion_Operaciones'),	
	path('eliminar_localizacion_operaciones/<int:pk>', Vistas_Base.LocalizacionOperaciones_DeleteView.as_view(template_name='eliminar_localizacion_operaciones.html'), name='Eliminar_Localizacion_Operaciones'),
	path('detalles_localizacion_operaciones/<int:pk>', Vistas_Base.LocalizacionOperaciones_DetailView.as_view(template_name='detalle_localizacion_operaciones.html'), name='Detalle_Localizacion_Operaciones'),

	path('listado_puntaje_departamentos/', Vistas_Base.Listado_Puntaje_Departamentos.as_view(template_name='listado_puntaje_departamentos.html'), name='Listado_Puntaje_Departamentos'),
	path('crear_listado_puntaje_departamentos/', Vistas_Base.Listado_Puntaje_Departamentos_CreateView.as_view(template_name='crear_listado_puntaje_departamentos.html'), name='Crear_Listado_Puntaje_Departamentos'),
	path('actualizar_listado_puntaje_departamentos/<int:pk>', Vistas_Base.Listado_Puntaje_Departamentos_UpdateView.as_view(template_name='actualizar_listado_puntaje_departamentos.html'), name='Actualizar_Listado_Puntaje_Departamentos'),	
	path('eliminar_listado_puntaje_departamentos/<int:pk>', Vistas_Base.Listado_Puntaje_Departamentos_DeleteView.as_view(template_name='eliminar_listado_puntaje_departamentos.html'), name='Eliminar_Listado_Puntaje_Departamentos'),
	path('detalles_listado_puntaje_departamentos/<int:pk>', Vistas_Base.Listado_Puntaje_Departamentos_DetailView.as_view(template_name='detalle_listado_puntaje_departamentos.html'), name='Detalle_Listado_Puntaje_Departamentos'),
	
	path('listado_documentacion_presentar/', Vistas_Base.ListadoTipo_DocumentoPresentar.as_view(template_name='listado_documento_presentar.html'), name='Listado_Documentacion_Presentar'),
	path('crear_documentacion_presentar/', Vistas_Base.Tipo_DocumentoPresentar_CreateView.as_view(template_name='crear_documento_presentar.html'), name='Crear_Documentacion_Presentar'),
	path('actualizar_documentacion_presentar/<int:pk>', Vistas_Base.Tipo_DocumentoPresentar_UpdateView.as_view(template_name='actualizar_documento_presentar.html'), name='Actualizar_Documentacion_Presentar'),	
	path('eliminar_documentacion_presentar/<int:pk>', Vistas_Base.Tipo_DocumentoPresentar_DeleteView.as_view(template_name='eliminar_documento_presentar.html'), name='Eliminar_Documentacion_Presentar'),
	path('detalles_documentacion_presentar/<int:pk>', Vistas_Base.Tipo_DocumentoPresentar_DetailView.as_view(template_name='detalle_documento_presentar.html'), name='Detalle_Documentacion_Presentar'),

	path('listado_exportaciones_bienes_servicios/', Vistas_Base.ListadoExp_Bienes_Servicios.as_view(template_name='listado_exp_bienes_servicios.html'), name='Listado_Exportaciones_Bienes_Servicios'),
	path('crear_exportaciones_bienes_servicios/', Vistas_Base.Exp_Bienes_Servicios_CreateView.as_view(template_name='crear_exp_bienes_servicios.html'), name='Crear_Exportaciones_Bienes_Servicios'),
	path('actualizar_exportaciones_bienes_servicios/<int:pk>', Vistas_Base.Exp_Bienes_Servicios_UpdateView.as_view(template_name='actualizar_exp_bienes_servicios.html'), name='Actualizar_Exportaciones_Bienes_Servicios'),	
	path('eliminar_exportaciones_bienes_servicios/<int:pk>', Vistas_Base.Exp_Bienes_Servicios_DeleteView.as_view(template_name='eliminar_exp_bienes_servicios.html'), name='Eliminar_Exportaciones_Bienes_Servicios'),
	path('detalles_exportaciones_bienes_servicios/<int:pk>', Vistas_Base.Exp_Bienes_Servicios_DetailView.as_view(template_name='detalle_exp_bienes_servicios.html'), name='Detalle_Exportaciones_Bienes_Servicios'),

	#path('cotizaciones_automaticas/', Vistas_WS.CotizacionesAutomaticasUpdateView.as_view(template_name='cotizaciones.html'), name='Cotizaciones_Automaticas'),
	##path('escoger_cotizaciones_automaticas/', Vistas_WS.EscogerCotizacionesAutomaticas.as_view(), name='Escoger_Cotizaciones_Automaticas'),
	#path('cotizaciones_automaticas/<uuid:csrfmiddlewaretoken>/<slug:fdesde>/<slug:fhasta>/', Vistas_WS.CotizacionesAutomaticasCreateView.as_view(template_name='cotizaciones.html'), name='Cotizaciones_Automaticas_Fechas'),
	#<slug:fdesde>/<slug:fhasta>/<uuid:csrfmiddlewaretoken> <slug:uidb64>/<slug:token>/<slug:key>/
	




]