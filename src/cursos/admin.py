from django.contrib import admin
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

class ClaseAdmin(admin.ModelAdmin):
	
	list_filter = (CountryFilter,)

	ordering = ['sorting', ]
	list_editable = ['sorting', ] 
	list_display = ['nombre', 'curso', 'sorting', ]
	readonly_fields = ['clase_slug', 'sorting', ]

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

admin.site.register(Area, AreaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Clase, ClaseAdmin)
