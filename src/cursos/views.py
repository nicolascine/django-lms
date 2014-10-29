from django.shortcuts import render, render_to_response, RequestContext, redirect
from cursos.models import Unidad, Curso, Clase
from examenes.models import *
from django.db import models

def home(request):
	return render_to_response("home.html", 
							  locals(), 
							  context_instance = RequestContext(request))

def cursos(request):
	todos_los_cursos = Curso.objects.all()
	return render_to_response("cursos.html", 
							  locals(), 
							  context_instance = RequestContext(request))

def cursodetalle(request, slug):
	curso = Curso.objects.get(slug=slug)
	unidad = Unidad.objects.filter(curso_id=curso.id)
	
	listado_clases = Clase.objects.filter(unidad_id__in=unidad, curso_id=curso.id).order_by('unidad', 'sorting')
	
	unidades = []
	for u in listado_clases:
		 unidades.append(u.unidad.id)
	unidades = list(set(unidades))

	listado_examenes = Examen.objects.filter(curso_id=curso.id)
	
	return render_to_response("curso_detalle.html", 
							  locals(), 
							  context_instance = RequestContext(request))

def clasedetalle(request, slug, clase_slug):
	if not request.user.is_authenticated():
		#return HttpResponse("Necesitas Loguearte!")
		 return redirect('/cuentas/entrar/')
	else:
		#listado_clases = Clase.objects.filter(curso=curso_id)
		curso = Curso.objects.get(slug=slug)
		unidad = Unidad.objects.filter(curso_id=curso.id)
		clase = Clase.objects.get(clase_slug=clase_slug)

		def clase_siguiente(numero):
			try:
				next = Clase.objects.get(curso_id = clase.curso.id, sorting=(numero+1))
				return next
			except Clase.DoesNotExist:
				return None
		
		def clase_anterior(numero):
			try:
				prev = Clase.objects.get(curso = clase.curso.id, sorting=(numero-1))
				return prev
			except Clase.DoesNotExist:
				return None
		
		listado_clases = Clase.objects.filter(unidad_id__in=unidad, curso_id=curso.id).order_by('sorting', 'nombre')
		siguiente = clase_siguiente(clase.sorting)
		anterior = clase_anterior(clase.sorting)

	return render_to_response("clase_detalle.html", 
								  locals(), 
								  context_instance = RequestContext(request))

def suscribirme(request, curso_id):
	curso = Curso.objects.get(id=curso_id)
	return render_to_response("suscribirme.html", 
							  locals(), 
							  context_instance = RequestContext(request))	
