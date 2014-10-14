from django.db import models
from django.utils.encoding import smart_unicode

from django.template.defaultfilters import slugify ## FRIENDLY SLUG <---


# Create your models here.


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
	
	def save(self, *args, **kwargs): #Then override models save method:

		#if not self.id:
		#Only set the slug when the object is created.
		self.slug = slugify(self.nombre) #Or whatever you want the slug to use
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
	sorting = models.IntegerField("Orden", blank=True, null=False, 
		help_text="Numero para ordenar clases")

	def save(self, *args, **kwargs): #Then override models save method:
		#if not self.id:
		#Only set the slug when the object is created.
		self.clase_slug = slugify(self.nombre) #Or whatever you want the slug to use
		super(Clase, self).save(*args, **kwargs)

	def __unicode__(self):
		return smart_unicode(self.nombre)
		
	class Meta:
		ordering = ('sorting', 'nombre')





