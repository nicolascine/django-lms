import datetime
from django.utils import timezone
from django import forms
from django.contrib import admin
from functools import update_wrapper, partial
from django.forms.models import (modelform_factory, modelformset_factory,
                                 inlineformset_factory, BaseInlineFormSet)
from django.contrib.admin import ModelAdmin, SimpleListFilter
from .models import Area, Curso, Clase, Unidad

class CursoFilter(SimpleListFilter):
    title = 'curso' # or use _('curso') for translated title
    parameter_name = 'curso'
    
    def lookups(self, request, model_admin):
        cuursos = set([c.curso for c in model_admin.model.objects.all()])
        return [(c.id, c.nombre) for c in cuursos]
	
	def queryset(self, request, queryset):
		if self.value():
			return queryset.filter(curso__id__exact=self.value())
		else:
			return queryset


# admin.py
class CountryFilter(SimpleListFilter):
    title = 'curso' # or use _('country') for translated title
    parameter_name = 'curso'

    def lookups(self, request, model_admin):
        countries = set([c.curso for c in model_admin.model.objects.all()])
        return [(c.id, c.nombre) for c in countries]
        # You can also use hardcoded model name like "Country" instead of 
        # "model_admin.model" if this is not direct foreign key filter

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(curso__id__exact=self.value())
        else:
            return queryset

#
#
class AreaAdmin(admin.ModelAdmin):
	class Meta:
		model = Area


## VARIABLES GLOBALES VALIDACION Posicion de clases
global arreglo
arreglo = []

def validaPosicion(n):
	#print "count vale:", count
	obj = Clase.objects.filter(curso_id=n)
	total = Clase.objects.filter(curso_id=n).count()
	#print "el total de clases es: ", total
	for p in obj:
		arreglo.append(p.sorting)
	#return arreglo

class ListaClaseForm(forms.ModelForm):

  	class Meta:
		model = Clase
	
	

 	def clean_sorting(self):
 		

		"""

		if Clase.objects.filter(curso_id=self.instance.curso.id, sorting=(self.cleaned_data['sorting'])):
			print('existe un registro igual:', str(self.cleaned_data['sorting']))
 		---->
		def funciona(n):
			if count + 1 == 2:
				print "count +1 == 2"
			arreglo.append(n)

		k = Clase.objects.filter(curso_id=self.instance.curso.id)
		
		for r in k:
			funciona(r.sorting)
			#print self.cleaned_data['sorting']
		
		cuenta = Clase.objects.filter(curso_id=self.instance.curso.id, sorting=(self.cleaned_data['sorting'])).count()
		todos = Clase.objects.filter(curso_id=self.instance.curso.id, sorting=(self.cleaned_data['sorting']))
		for registro in todos:
			if cuenta > 1 and self.cleaned_data['sorting'] == registro.sorting:
				raise forms.ValidationError("Ya existe este registro")
		"""
		"""
		for solo in todos:
			if cuenta>1 and self.cleaned_data['sorting']==solo.sorting:
				raise forms.ValidationError("este error si funciona :) ")

		for t in p:
			#ahora = timezone.now()
			if (self.cleaned_data['sorting'] == t.sorting and t.updated > ahora):
				raise forms.ValidationError("esto ya existe")
		"""		
		return self.cleaned_data['sorting']

		#arreglo = Clase.objects.filter(curso_id=self.instance.curso.id)
		#print arreglo

		"""
		if Clase.objects.filter(curso_id=self.instance.curso.id, sorting=self.cleaned_data['sorting']):
			print Clase.objects.filter(curso_id=self.instance.curso.id, sorting=self.cleaned_data['sorting'])
			raise forms.ValidationError("esto ya existe")
		return self.cleaned_data['sorting']
		"""
class ClaseAdmin(admin.ModelAdmin):

	form = ListaClaseForm

	list_filter = (CountryFilter,)
	ordering = ['sorting', ]
	list_editable = ['sorting', ] 
	list_display = ['nombre', 'curso', 'sorting', ]
	readonly_fields = ['clase_slug', 'sorting', ]

	def get_changelist_formset(self, request, **kwargs):
	 		
	 		if request.GET and request.GET['curso']:
	 			del arreglo[:]
	 			#print request.GET['curso']
				validaPosicion(request.GET['curso'])
	 			print "arreglo en el GET: ", arreglo
	 		"""
			if request.POST:
				try:
					del arreglo[:]
					print "cambio el curso ------->"
					print "el valor del arreglo AHORA ESSSSS: ", arreglo
				except Exception, e:
					pass

				for x in xrange(0,int(request.POST['form-TOTAL_FORMS'])):
					validaPosicion(request.POST['form-'+str(x)+'-sorting'])
					pass
			"""
				#print "existe un total de:", request.POST['form-TOTAL_FORMS'], "registros"
				#print request.POST
			"""
	 		try:
	 			curso = request.GET['curso']
	 			validaPosicion(curso)
	 		except Exception, e:
	 			pass
			"""
			defaults = {
	            "formfield_callback": partial(super(ClaseAdmin, self).formfield_for_dbfield, request=request),
	            "form": ListaClaseForm,
	        }
			defaults.update(kwargs)
	 		#print "el ID del curso es --->>>>", self.curso.id
			return modelformset_factory(Clase,
	                                    extra=0,
	                                    fields=self.list_editable, **defaults)


class UnidadInline(admin.TabularInline):	
	model = Unidad

	class Meta:
		model = Unidad

class CursoAdmin(admin.ModelAdmin):
	inlines = [
        UnidadInline,
    ]
	readonly_fields = ('slug',)

	class Meta:
		model = Curso

admin.site.register(Area, AreaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Clase, ClaseAdmin)
