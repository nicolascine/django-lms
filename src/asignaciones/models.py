from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User 
import cursos


# Create your models here.

class Asignacion(models.Model):
	user = models.ForeignKey(User, null=False, blank=False)
	
	curso = models.ManyToManyField(cursos.models.Curso, through='Orden', null=True, blank=False)
	fecha_incio = models.DateTimeField(auto_now_add=False, auto_now=False)
	total_dias = models.IntegerField(blank=False, null=False, choices=[(30, 30), (60, 60), (5, 5)]) 

	aprobacion_admin = models.NullBooleanField()

	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
	
	class Meta:
		verbose_name_plural = "Asignaciones"

	def __unicode__(self):
			return smart_unicode(self.user)
			#return '%s | %s ' % (self.user, self.curso)

class Orden(models.Model):

	nombre = models.CharField(null=True, blank=True, max_length=50)
	user = models.ForeignKey(User, null=False, blank=False)
	curso = models.ForeignKey(cursos.models.Curso, null=False, blank=False)
	asignacion = models.ForeignKey(Asignacion, null=False, blank=False)
	
 	class Meta:
			unique_together = ['user', 'asignacion']

	def __unicode__(self):
			#return smart_unicode(self.nombre)
			return '%s | %s ' % (self.user, self.curso)