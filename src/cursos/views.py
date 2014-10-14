from django.shortcuts import render, render_to_response, RequestContext, redirect
from cursos.models import Curso, Clase


# Create your views here.

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
	listado_clases = Clase.objects.filter(curso=curso.id).order_by('sorting', 'nombre')
	return render_to_response("curso_detalle.html", 
							  locals(), 
							  context_instance = RequestContext(request))

def clasedetalle(request, slug, clase_slug):
	if not request.user.is_authenticated():
		#return HttpResponse("Necesitas Loguearte!")
		 return redirect('/cuentas/entrar/')
	else:

		#listado_clases = Clase.objects.filter(curso=curso_id)
		clase = Clase.objects.get(clase_slug=clase_slug)
		#curso_id = curso_id

		return render_to_response("clase_detalle.html", 
								  locals(), 
								  context_instance = RequestContext(request))

def suscribirme(request, curso_id):
	curso = Curso.objects.get(id=curso_id)
	return render_to_response("suscribirme.html", 
							  locals(), 
							  context_instance = RequestContext(request))		