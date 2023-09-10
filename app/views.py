from django.shortcuts import render
from api.models import Dificultad,Genero,Cancion,CapturaCancion
from django.db.models import Count
import json

def index(request):
    #verificar registros
    cantidad_dificultades = Dificultad.objects.all().count()
    cantidad_generos = Genero.objects.all().count()

    if cantidad_dificultades == 0 and cantidad_generos == 0:

        print("[!] Se registraron las dificultades y los genéros en la base de datos")

        Dificultad.objects.create(nombre="Fácil")
        Dificultad.objects.create(nombre="Intermedio")
        Dificultad.objects.create(nombre="Difícil")

        Genero.objects.create(nombre="Rock")
        Genero.objects.create(nombre="Hard rock")
        Genero.objects.create(nombre="Metal")
        Genero.objects.create(nombre="Pop")
        Genero.objects.create(nombre="Punk")
        Genero.objects.create(nombre="Folk")
        Genero.objects.create(nombre="Blues")
        Genero.objects.create(nombre="Country")
        Genero.objects.create(nombre="Soul")
        Genero.objects.create(nombre="Jazz")
        Genero.objects.create(nombre="Otro")

    print("[!] Los datos de dificultades y genéros son los siguientes")
    generos = Genero.objects.all()
    dificultades = Dificultad.objects.all()

    for dificultad in dificultades:
        print("Dificultad : %s" % (dificultad,))

    for genero in generos:
        print("Genéro : %s" % (genero,))

    return render(request, "app/index.html", {"dificultades":dificultades,"generos":generos})

def capturas(request,id_tutorial):
    return render(request, "app/capturas.html", {"id_tutorial":id_tutorial})

def generar(request,id_tutorial):
    return render(request, "app/generar.html", {"id_tutorial":id_tutorial})

def estadisticas(request):
        
    textos_grafico1 = []
    series_grafico1 = []

    canciones = Cancion.objects.all()
    cantidad_canciones = len(canciones)
    dificultades = Dificultad.objects.annotate(cantidad=Count('cancion'))

    for dificultad in dificultades:
        nombre_dificultad = dificultad.nombre
        cantidad = dificultad.cantidad
        textos_grafico1.append(nombre_dificultad)
        data = {'name':nombre_dificultad,'y':cantidad} 
        series_grafico1.append(data)

    json_texto_grafico1 = json.dumps(textos_grafico1)
    json_series_grafico1 = json.dumps(series_grafico1)

    ##

    textos_grafico2 = []
    series_grafico2 = []

    canciones = Cancion.objects.all()
    cantidad_canciones = len(canciones)
    generos = Genero.objects.annotate(cantidad=Count('cancion'))

    for genero in generos:
        nombre_genero = genero.nombre
        cantidad = genero.cantidad
        if cantidad > 0:
            textos_grafico2.append(nombre_genero)
            data = {'name':nombre_genero,'y':cantidad} 
            series_grafico2.append(data)

    json_texto_grafico2 = json.dumps(textos_grafico2)
    json_series_grafico2 = json.dumps(series_grafico2)

    return render(request, 'app/estadisticas.html', {'cantidad_canciones':cantidad_canciones,
                                                     'textos_grafico1':json_texto_grafico1,'series_grafico1':json_series_grafico1,
                                                     'textos_grafico2':json_texto_grafico2,'series_grafico2':json_series_grafico2})

def about(request):
    return render(request, "app/about.html", {})