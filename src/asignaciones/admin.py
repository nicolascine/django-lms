from django.contrib import admin

# Register your models here.

from .models import Asignacion, Orden


class AsignacionAdmin(admin.ModelAdmin):
	class Meta:
		model = Asignacion

class OrdenAdmin(admin.ModelAdmin):
	class Meta:
		model = Orden

# Registro modelsAdmin

admin.site.register(Asignacion, AsignacionAdmin)
admin.site.register(Orden, OrdenAdmin)