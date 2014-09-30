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

def cursodetalle(request, curso_id):
	curso = Curso.objects.get(id=curso_id)
	listado_clases = Clase.objects.filter(curso=curso_id)
	return render_to_response("curso_detalle.html", 
							  locals(), 
							  context_instance = RequestContext(request))

def clasedetalle(request, curso_id, clase_id):
	if not request.user.is_authenticated():
		#return HttpResponse("Necesitas Loguearte!")
		 return redirect('/cuentas/entrar/')
	else:

		clase = Clase.objects.get(id=clase_id)
		listado_clases = Clase.objects.filter(curso=curso_id)
		curso_id = curso_id

		return render_to_response("clase_detalle.html", 
								  locals(), 
								  context_instance = RequestContext(request))

def suscribirme(request, curso_id):
	curso = Curso.objects.get(id=curso_id)
	return render_to_response("suscribirme.html", 
							  locals(), 
							  context_instance = RequestContext(request))		