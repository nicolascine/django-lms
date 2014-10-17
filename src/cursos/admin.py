from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.contrib.admin import ModelAdmin
from .models import Area, Curso, Clase, Unidad


class CursoFilter(SimpleListFilter):
    title = 'curso' # or use _('curso') for translated title
    parameter_name = 'curso'

    def lookups(self, request, model_admin):
        cursos = set([c.curso for c in model_admin.model.objects.all()])
        return [(c.id, c.nombre) for c in cursos]
        # You can also use hardcoded model name like "Curso" instead of 
        # "model_admin.model" if this is not direct foreign key filter

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(curso__id__exact=self.value())
        else:
            return queryset


class AreaAdmin(admin.ModelAdmin):
	class Meta:
		model = Area

class ClaseAdmin(admin.ModelAdmin):
	
	list_filter = (CursoFilter,)
	ordering = ['nombre', 'sorting', 'curso', ]
	list_editable = ['sorting', ] 
	list_display = ['nombre', 'sorting', 'curso', ]
	readonly_fields = ('clase_slug',)

	
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
	readonly_fields = ('slug',)

	class Meta:
		model = Curso


# Registro modelsAdmin #

admin.site.register(Area, AreaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Clase, ClaseAdmin)
#admin.site.register(Unidad, UnidadAdmin)