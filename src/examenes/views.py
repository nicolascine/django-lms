from django.shortcuts import render, render_to_response, RequestContext, redirect
from cursos.models import Unidad, Curso, Clase
from examenes.models import Examen, PreguntaEnExamen, Pregunta, Respuesta, RespuestasDelUsuario
from django.db import models


"""imports para Formu Examen """
from forms import UsuarioFormuRespuestas
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

def examandetalle(request, slug, examen_slug):
	if not request.user.is_authenticated():
		#return HttpResponse("Necesitas Loguearte!")
		return redirect('/cuentas/entrar/')
	else:
		examen = Examen.objects.get(examen_slug=examen_slug)
		curso = Curso.objects.get(slug=slug)
		preguntaDelExamen = PreguntaEnExamen.objects.filter(examen_id=examen.id)
		arregloPreguntas = []
		for K in preguntaDelExamen:
			arregloPreguntas.append(K.pregunta_id)

		listado_preguntas = Pregunta.objects.filter(id__in = arregloPreguntas)
		
	return render_to_response("examen_detalle.html", 
							  locals(),
							  context_instance = RequestContext(request))

def preguntadetalle(request, slug, examen_slug, pregunta_id):
	if not request.user.is_authenticated():
		 return redirect('/cuentas/entrar/')
	else:
		curso = Curso.objects.get(slug=slug)
		examen = Examen.objects.get(examen_slug=examen_slug)
		pregunta = Pregunta.objects.get(id=pregunta_id)
		pregenExam = PreguntaEnExamen.objects.get(pregunta_id = pregunta.id)

		def pregunta_siguiente(numero):
			try:
				obj = PreguntaEnExamen.objects.get(examen_id = examen.id, sorting=(numero+1))
				next = Pregunta.objects.get(preguntaenexamen = obj.id)
				return next
			except PreguntaEnExamen.DoesNotExist:
				return None

		def pregunta_anterior(numero):
			try:
				obj = PreguntaEnExamen.objects.get(examen_id = examen.id, sorting=(numero-1))
				prev = Pregunta.objects.get(preguntaenexamen = obj.id)
				return prev
			except PreguntaEnExamen.DoesNotExist:
				return None

		siguiente = pregunta_siguiente(pregenExam.sorting)
		anterior = pregunta_anterior(pregenExam.sorting)
		
		listado_respuestas = Respuesta.objects.filter(pregunta_id=pregunta.id)

		""" IF IS POST (SEND ANSWER) """

		marca = RespuestasDelUsuario.objects.filter(pregunta_id = pregunta_id, user_id = request.user.id)

		for m in marca:
			print m.respuesta_id

		if request.POST:
			form = UsuarioFormuRespuestas(request.POST)
			if form.is_valid():
				obj = form.save(commit=False)
				obj.user = request.user
				obj.pregunta = pregunta
				obj.save()
				#return HttpResponseRedirect('/')
		else:
		    form = UsuarioFormuRespuestas()
		 
		args = {}
		args.update(csrf(request))
		
		args['form'] = form

		return render_to_response("pregunta_detalle.html", 
								  locals(),
								  context_instance = RequestContext(request))
