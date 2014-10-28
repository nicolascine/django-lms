from django.shortcuts import render, render_to_response, RequestContext, redirect
from cursos.models import Unidad, Curso, Clase
from examenes.models import *
from django.db import models


def examandetalle(request, slug, examen_slug):
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
	curso = Curso.objects.get(slug=slug)
	examen = Examen.objects.get(examen_slug=examen_slug)
	pregunta = Pregunta.objects.get(id=pregunta_id)

	listado_respuestas = Respuesta.objects.filter(pregunta_id=pregunta.id)
	return render_to_response("pregunta_detalle.html", 
							  locals(),
							  context_instance = RequestContext(request))