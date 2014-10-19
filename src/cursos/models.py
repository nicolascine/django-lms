from django.db import models
from django.db.models import Max
from django.utils.encoding import smart_unicode
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django import forms

class Area(models.Model):
	nombre = models.CharField(null=False, blank=False, max_length=200)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
	def __unicode__(self):
			return smart_unicode(self.nombre)

class Curso(models.Model):
	nombre = models.CharField(null=False, blank=False, max_length=200, unique=True)
	slug = models.SlugField(('slug'), max_length=60, blank=True, unique=True)
	area = models.ForeignKey(Area)
	img = models.ImageField(upload_to='cursos', blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		super(Curso, self).save(*args, **kwargs)

	def __unicode__(self):
		return smart_unicode(self.nombre)

class Unidad(models.Model):
	nombre = models.CharField(null=False, blank=False, max_length=200)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	curso = models.ForeignKey(Curso)
	
	class Meta:
		verbose_name_plural = "Unidades"

	def __unicode__(self):
		return smart_unicode(self.nombre)

class Clase(models.Model):
	curso = models.ForeignKey(Curso)
	unidad = models.ForeignKey(Unidad)
	nombre = models.CharField(null=False, blank=False, max_length=200, unique=True)
	clase_slug = models.SlugField(('slug'), max_length=60, blank=True, unique=True)
	contenido = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	sorting = models.IntegerField("Orden", blank=False, null=False,
		help_text="Numero para ordenar clases")

	

	def save(self, *args, **kwargs):



		self.clase_slug = slugify(self.nombre)
			
		# logica: si no existe ID (solo cuando se crea el objeto), busca el ultimo numero(sorting)
		# y se incrementa en 1. Si es la primera clase del curso reemplaza el sorting__max = None, por int(0),
		# quedando con sorting = 1
		
		ultimo = Clase.objects.filter(curso_id=self.curso.id).aggregate(Max('sorting'))

		if not self.id:
			if ultimo['sorting__max'] == None:
				ultimo['sorting__max'] = 0
			self.sorting = (ultimo['sorting__max']) + 1
		else:
			if Clase.objects.filter(curso_id=self.curso.id, sorting=self.sorting):
				#raise forms.ValidationError('%s ya esta en la lisssssta' % self.sorting)
				raise forms.ValidationError("You have no points!")
				
		super(Clase, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return smart_unicode(self.nombre)

	class Meta:
		ordering = ('sorting', 'nombre')

#Online Exam Model

class Exam(models.Model):
    class Meta:
        verbose_name = ('Exam')
        verbose_name_plural = ('Exams')

    def __unicode__(self):
        pass

class Question(models.Model):
    class Meta:
        verbose_name = ('Question')
        verbose_name_plural = ('Questions')

    def __unicode__(self):
        pass

class ValidAnswer(models.Model):
    class Meta:
        verbose_name = ('ValidAnswer')
        verbose_name_plural = ('ValidAnswers')

    def __unicode__(self):
        pass
    
class QuestioninExam(models.Model):
    class Meta:
        verbose_name = ('QuestioninExam')
        verbose_name_plural = ('QuestionsinExams')

    def __unicode__(self):
        pass
    
class UserAssesment(models.Model):
    class Meta:
        verbose_name = ('UserAssesment')
        verbose_name_plural = ('UserAssesments')

    def __unicode__(self):
        pass
