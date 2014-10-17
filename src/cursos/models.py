from django.db import models
from django.db.models import Max
from django.utils.encoding import smart_unicode
from django.template.defaultfilters import slugify

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
		#if not self.id:
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
		if not self.id:
			ultimo = Clase.objects.filter(curso_id=self.curso.id).aggregate(Max('sorting'))
			self.sorting = (ultimo['sorting__max']) + 1
		super(Clase, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return smart_unicode(self.nombre)

	class Meta:
		ordering = ('sorting', 'nombre')
