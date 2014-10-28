from django.shortcuts import render, render_to_response, RequestContext, redirect
from cursos.models import Unidad, Curso, Clase
from examenes.models import *
from django.db import models


def examandetalle(request, slug, examen_slug):
	examen = Examen.objects.get(examen_slug=examen_slug)
	curso = Curso.objects.get(slug=slug)

	return render_to_response("examen_detalle.html", 
							  locals(),
							  context_instance = RequestContext(request))