from django.shortcuts import render
from api.models import Cancion,CapturaCancion

def index(request):
    return render(request, 'app/index.html', {})

def capturas(request,id_tutorial):
    return render(request, 'app/capturas.html', {"id_tutorial":id_tutorial})

def generar(request,id_tutorial):
    return render(request, 'app/generar.html', {"id_tutorial":id_tutorial})