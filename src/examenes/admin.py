from django import forms
from django.contrib import admin
from functools import update_wrapper, partial
from django.forms.models import (modelform_factory, modelformset_factory,inlineformset_factory, BaseInlineFormSet)
from .models import Examen, Pregunta, PreguntaEnExamen, Respuesta

class RespuestaForm(forms.ModelForm):

	class Meta:
		model = Respuesta

	def clean_correcto(self):
		if self.cleaned_data['correcto'] == True:
			k = Respuesta.objects.filter(pregunta_id=self.instance.pregunta_id)
			for p in k:
				if self.cleaned_data['correcto'] == p.correcto and self.instance.id != p.id:
					raise forms.ValidationError("Ya existe una respuesta correcta")
		
		return self.cleaned_data['correcto']

class RespuestaInline(admin.TabularInline):
	model = Respuesta
	form = RespuestaForm
	def get_changelist_formset(self, request, **kwargs):
	 		
			defaults = {
	            "formfield_callback": partial(super(RespuestaInline, self).formfield_for_dbfield, request=request),
	            "form": RespuestaForm,
	        }
			defaults.update(kwargs)

			return modelformset_factory(Respuesta,extra=0,fields=self.list_editable, **defaults)

class PreguntaAdmin(admin.ModelAdmin):
	
	model = Pregunta
	inlines = [ RespuestaInline,]

	class Meta:
		model = Pregunta

class PreguntaEnExamenForm(forms.ModelForm):

	def clean_sorting(self):
		k = PreguntaEnExamen.objects.filter(examen_id=self.instance.examen.id)
		for p in k:
			if p.sorting == self.cleaned_data['sorting'] and p.id != self.instance.id:
				raise forms.ValidationError("Otra pregunta utiliza la posicion %s" % self.cleaned_data['sorting'])
		return self.cleaned_data['sorting']

	class Meta:
		model = PreguntaEnExamen


class PreguntaEnExamenInline(admin.TabularInline):

	model = PreguntaEnExamen
	form = PreguntaEnExamenForm

	def get_changelist_formset(self, request, **kwargs):
			defaults = {
	            "formfield_callback": partial(super(PreguntaEnExamenInline, self).formfield_for_dbfield, request=request),
	            "form": PreguntaEnExamenForm,
	        }
			defaults.update(kwargs)
			return modelformset_factory(PreguntaEnExamen,extra=0,fields=self.list_editable, **defaults)
	
	class Meta:
		model = PreguntaEnExamen


class ExamenAdmin(admin.ModelAdmin):

	readonly_fields = ['examen_slug', ]
	inlines = [PreguntaEnExamenInline,]

	class Meta:
		model = Examen

admin.site.register(Respuesta)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Examen, ExamenAdmin)