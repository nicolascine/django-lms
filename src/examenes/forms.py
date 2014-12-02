from django import forms
from examenes.models import *

class UsuarioFormuRespuestas(forms.ModelForm):
	

	def clean(self):
		
		cleaned_data = self.cleaned_data
		respuesta = cleaned_data.get("respuesta")
		if respuesta == None:
			raise forms.ValidationError("Debes seleccionar una respuesta")
		return cleaned_data

	class Meta:
		model = RespuestasDelUsuario
		exclude = ['user', 'pregunta']
