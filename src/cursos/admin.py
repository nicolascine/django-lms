from django.contrib import admin

# Register your models here.

from .models import Area, Curso, Clase, Unidad


class AreaAdmin(admin.ModelAdmin):
	class Meta:
		model = Area

class ClaseAdmin(admin.ModelAdmin):
	
	ordering = ['sorting', 'nombre', ]
	list_editable = ['sorting', ] 
	list_display = ['nombre', 'sorting', ] 
	
	class Meta:
		model = Clase

class UnidadInline(admin.TabularInline):	
	
	model = Unidad

	class Meta:
		model = Unidad

class CursoAdmin(admin.ModelAdmin):
	
	inlines = [
        UnidadInline,
    ]

	class Meta:
		model = Curso


# Registro modelsAdmin #

admin.site.register(Area, AreaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Clase, ClaseAdmin)
#admin.site.register(Unidad, UnidadAdmin)