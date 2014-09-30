from django.contrib import admin

# Register your models here.

from .models import Area, Curso, Clase, Unidad


class AreaAdmin(admin.ModelAdmin):
	class Meta:
		model = Area

class CursoAdmin(admin.ModelAdmin):
	class Meta:
		model = Curso

class ClaseAdmin(admin.ModelAdmin):
	class Meta:
		model = Clase

class UnidadAdmin(admin.ModelAdmin):
	class Meta:
		model = Unidad
		

# Registro modelsAdmin #

admin.site.register(Area, AreaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Clase, ClaseAdmin)
admin.site.register(Unidad, UnidadAdmin)