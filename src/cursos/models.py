from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.


class Area(models.Model):
	nombre = models.CharField(null=False, blank=False, max_length=200)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
	def __unicode__(self):
			return smart_unicode(self.nombre)

class Curso(models.Model):
	nombre = models.CharField(null=False, blank=False, max_length=200)
	area = models.ForeignKey(Area)
	img = models.ImageField(upload_to='cursos', blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

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
	nombre = models.CharField(null=False, blank=False, max_length=200)
	contenido = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return smart_unicode(self.nombre)