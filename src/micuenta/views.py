from django.shortcuts import render, render_to_response, RequestContext, redirect
from micuenta.models import UserProfile
from asignaciones.models import Asignacion


# Create your views here.

def getAsignaciones(user_id):
	miscursos = Asignacion.objects.filter(user=user_id)
	return miscursos
	
def micuenta(request):
	if not request.user.is_authenticated():
		#return HttpResponse("Necesitas Loguearte!")
		 return redirect('/cuentas/entrar/')
	else:
		miscursos = getAsignaciones(request.user.id) 
		return render_to_response("micuenta.html", 
							  locals(), 
							  context_instance = RequestContext(request))