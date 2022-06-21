from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from administrativo.models import Matricula

# vista que permita presesentar las matriculas
# el nombre de la vista es index.

def index(request):
    """

    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    matri = Matricula.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'matriculas': matri, 'numero_matriculas': len(matri)}
    return render(request, 'index.html', informacion_template)
