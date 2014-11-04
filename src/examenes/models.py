from django.db import models
from django.db.models import Max
from django.utils.encoding import smart_unicode
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User 
from cursos.models import Curso, Unidad


class Examen(models.Model):
    curso = models.ForeignKey(Curso)
    unidad = models.ForeignKey(Unidad)
    nombre = models.CharField(blank=False, null=False, unique=True, max_length=250)
    descripcion = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    examen_slug = models.SlugField(('slug'), max_length=60, blank=True, unique=True)

    def save(self, *args, **kwargs):
            self.examen_slug = slugify(self.nombre)
            super(Examen, self).save(*args, **kwargs)
   
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
    tipo = models.CharField(max_length=20, choices=TIPOS_PREGUNTA, default='A')
    texto = models.TextField()
    
    class Meta:
        verbose_name = ('Pregunta')
        verbose_name_plural = ('Preguntas')

    def __unicode__(self):
        return smart_unicode(self.texto)
        

class PreguntaEnExamen(models.Model):
    examen = models.ForeignKey(Examen)
    pregunta = models.ForeignKey(Pregunta)
    sorting = models.IntegerField("Orden", blank=True, null=False,
        help_text="Numero para ordenar Preguntas")
    
    def save(self, *args, **kwargs):
        ultima = PreguntaEnExamen.objects.filter(examen_id=self.examen.id).aggregate(Max('sorting'))
        if not self.id: 
            if ultima['sorting__max'] == None:
                ultima['sorting__max'] = 0
            self.sorting = (ultima['sorting__max']) + 1
        super(PreguntaEnExamen, self).save(*args, **kwargs)

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
    

