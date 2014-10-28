from django.db import models
from django.utils.encoding import smart_unicode
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User 
from cursos.models import Curso


class Examen(models.Model):
    curso = models.ForeignKey(Curso)
    nombre = models.CharField(blank=False, null=False, unique=True, max_length=250)
    descripcion = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = ('Examen')
        verbose_name_plural = ('Examenes')
    
    def __unicode__(self):
        return smart_unicode(self.nombre)
   
class Pregunta(models.Model):
    TIPOS_PREGUNTA = (
        ('A', 'Alternativas'),
        ('VF', 'Verdadeo o Falso'),
        ('T', 'Texto Libre'),
    )
    tipo = models.CharField(max_length=20, choices=TIPOS_PREGUNTA)
    texto = models.TextField()
    
    class Meta:
        verbose_name = ('Pregunta')
        verbose_name_plural = ('Preguntas')

    def __unicode__(self):
        return smart_unicode(self.texto)
        

class PreguntaEnExamen(models.Model):
    examen = models.ForeignKey(Examen)
    pregunta = models.ForeignKey(Pregunta)

    class Meta:
        verbose_name = ('Pregunta del Examen')
        verbose_name_plural = ('Preguntas del Examen')

    def __unicode__(self):
        pass

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta)
    texto = models.TextField()
    correcto = models.NullBooleanField(default=False)

    class Meta:
        verbose_name = ('Respuesta')
        verbose_name_plural = ('Respuestas')

    def __unicode__(self):
        return smart_unicode(self.texto)
    

