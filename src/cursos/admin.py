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

class AreaAdmin(admin.ModelAdmin):
	class Meta:
		model = Area


class ListaClaseForm(forms.ModelForm):

  	class Meta:
		model = Clase
	
	def clean_sorting(self):
 		
		#print self.instance.id, "---", self.instance.sorting
		k = Clase.objects.filter(curso_id=self.instance.curso.id)
		for p in k:
			if p.sorting == self.cleaned_data['sorting'] and self.instance.id != p.id:
				raise forms.ValidationError("Otra clase utiliza la posicion %s" % self.cleaned_data['sorting'])
		return self.cleaned_data['sorting']

class ClaseAdmin(admin.ModelAdmin):

	form = ListaClaseForm

	list_filter = (CountryFilter,)
	ordering = ['sorting', ]
	list_editable = ['sorting', ] 
	list_display = ['nombre', 'curso', 'sorting', ]
	readonly_fields = ['clase_slug', 'sorting', ]

	def get_changelist_formset(self, request, **kwargs):
	 		
			defaults = {
	            "formfield_callback": partial(super(ClaseAdmin, self).formfield_for_dbfield, request=request),
	            "form": ListaClaseForm,
	        }
			defaults.update(kwargs)

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
