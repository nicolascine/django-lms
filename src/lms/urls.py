from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    

    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'cursos.views.home', name='home'),
    url(r'^cursos/$', 'cursos.views.cursos', name='cursos'),
    #url(r'^curso/(?P<curso_id>\d+)/$', 'cursos.views.cursodetalle', name='cursodetalle'),
    url(r'^cursos/(?P<slug>[-\w]+)/$', 'cursos.views.cursodetalle', name='cursodetalle'),
    #url(r'^cursos/(?P<curso_id>\d+)/clase/(?P<clase_id>\d+)/$', 'cursos.views.clasedetalle', name='clasedetalle'),
    url(r'^cursos/(?P<slug>[-\w]+)/(?P<clase_slug>[-\w]+)/', 'cursos.views.clasedetalle', name='clasedetalle'),
    url(r'^curso/suscribirme/(?P<curso_id>\d+)/', 'cursos.views.suscribirme', name='suscribirme'),


    url(r'^cuentas/', include('allauth.urls')),
    url(r'^micuenta/', 'micuenta.views.micuenta'),
)


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, 
							document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, 
							document_root=settings.MEDIA_ROOT)