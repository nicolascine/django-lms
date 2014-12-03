from django import forms
from examenes.models import *

class UsuarioFormuRespuestas(forms.ModelForm):
	

	def clean(self):
		
		cleaned_data = self.cleaned_data
		respuesta = cleaned_data.get("respuesta")
		#print "EN EL CLEAN: ", respuesta.id
		#if respuesta == None:
		#	raise forms.ValidationError("Debes seleccionar una respuesta")
		return cleaned_data

	class Meta:
		model = RespuestasDelUsuario
		exclude = ['user', 'pregunta']
		labels = {
		    'respuesta': ('Respuesta'),
		}
		help_texts = {
		    'respuesta': ('Selecciona una respuesta'),
		}
		error_messages = {
		    'respuesta': {
		        'required': ("Debes seleccionar una respuesta"),
		    },
		}
