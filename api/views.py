from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from api.models import Dificultad,Genero,Cancion,CapturaCancion

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

import base64
import time

from django.conf import settings

import os

@csrf_exempt
def listar_tutoriales(request):
    canciones = Cancion.objects.all().order_by("-id")
    listas = []
    for cancion in canciones:
        capturas = len(CapturaCancion.objects.filter(cancion_id=cancion.id))
        listas.append({"id":cancion.id, "titulo":cancion.titulo,"afinacion":cancion.afinacion,"dificultad":cancion.dificultad.nombre,"genero":cancion.genero.nombre,"link_youtube":cancion.link_youtube,"capturas":capturas,"fecha":cancion.fecha})
    return JsonResponse({"estado":200,"tutoriales": list(listas)})

@csrf_exempt
def listar_tutoriales_filtro_titulo(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    filtro = body["filtro"]
    canciones = []
    if filtro != "":
        canciones = Cancion.objects.filter(titulo__icontains=filtro).order_by("-id")
    else:
        canciones = Cancion.objects.all().order_by("-id")
    listas = []
    for cancion in canciones:
        capturas = len(CapturaCancion.objects.filter(cancion_id=cancion.id))
        listas.append({"id":cancion.id, "titulo":cancion.titulo,"afinacion":cancion.afinacion,"dificultad":cancion.dificultad.nombre,"genero":cancion.genero.nombre,"link_youtube":cancion.link_youtube,"capturas":capturas,"fecha":cancion.fecha})
    return JsonResponse({"estado":200,"tutoriales": list(listas)})

@csrf_exempt
def listar_tutoriales_filtro_afinacion(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    filtro = body["filtro"]
    canciones = []
    if filtro != "":
        canciones = Cancion.objects.filter(afinacion__icontains=filtro).order_by("-id")
    else:
        canciones = Cancion.objects.all().order_by("-id")
    listas = []
    for cancion in canciones:
        capturas = len(CapturaCancion.objects.filter(cancion_id=cancion.id))
        listas.append({"id":cancion.id, "titulo":cancion.titulo,"afinacion":cancion.afinacion,"dificultad":cancion.dificultad.nombre,"genero":cancion.genero.nombre,"link_youtube":cancion.link_youtube,"capturas":capturas,"fecha":cancion.fecha})
    return JsonResponse({"estado":200,"tutoriales": list(listas)})

@csrf_exempt
def listar_tutoriales_filtro_dificultad(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    filtro = body["filtro"]
    canciones = []
    if filtro != "":
        canciones = Cancion.objects.filter(dificultad_id=filtro).order_by("-id")
    else:
        canciones = Cancion.objects.all().order_by("-id")
    listas = []
    for cancion in canciones:
        capturas = len(CapturaCancion.objects.filter(cancion_id=cancion.id))
        listas.append({"id":cancion.id, "titulo":cancion.titulo,"afinacion":cancion.afinacion,"dificultad":cancion.dificultad.nombre,"genero":cancion.genero.nombre,"link_youtube":cancion.link_youtube,"capturas":capturas,"fecha":cancion.fecha})
    return JsonResponse({"estado":200,"tutoriales": list(listas)})

@csrf_exempt
def listar_tutoriales_filtro_genero(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    filtro = body["filtro"]
    canciones = []
    if filtro != "":
        canciones = Cancion.objects.filter(genero_id=filtro).order_by("-id")
    else:
        canciones = Cancion.objects.all().order_by("-id")
    listas = []
    for cancion in canciones:
        capturas = len(CapturaCancion.objects.filter(cancion_id=cancion.id))
        listas.append({"id":cancion.id, "titulo":cancion.titulo,"afinacion":cancion.afinacion,"dificultad":cancion.dificultad.nombre,"genero":cancion.genero.nombre,"link_youtube":cancion.link_youtube,"capturas":capturas,"fecha":cancion.fecha})
    return JsonResponse({"estado":200,"tutoriales": list(listas)})

@csrf_exempt
def listar_dificultades(request):
    queryset = Dificultad.objects.filter().order_by("id").values()
    return JsonResponse({"estado":200,"dificultades": list(queryset)})

@csrf_exempt
def listar_generos(request):
    queryset = Genero.objects.filter().order_by("id").values()
    return JsonResponse({"estado":200,"generos": list(queryset)})

@csrf_exempt
def cargar_tutorial(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    id_tutorial = body["id_tutorial"]
    queryset = Cancion.objects.filter(id=id_tutorial).values()
    return JsonResponse({"estado":200,"tutorial": list(queryset)})

@csrf_exempt
def agregar_tutorial(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    titulo = body["titulo"]
    afinacion = body["afinacion"]
    dificultad_id = body["dificultad_id"]
    link_youtube = body["link_youtube"]
    Cancion.objects.create(titulo=titulo,afinacion=afinacion,dificultad_id=dificultad_id,genero_id=1,link_youtube=link_youtube)
    return JsonResponse({"estado": "200","mensaje":"El tutorial fue guardado correctamente"})

@csrf_exempt
def editar_tutorial(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    id_tutorial = body["id_tutorial"]
    titulo = body["titulo"]
    afinacion = body["afinacion"]
    dificultad_id = body["dificultad_id"]
    genero_id = body["genero_id"]
    link_youtube = body["link_youtube"]
    Cancion.objects.filter(id=id_tutorial).update(titulo=titulo,afinacion=afinacion,dificultad_id=dificultad_id,genero_id=genero_id,link_youtube=link_youtube)
    return JsonResponse({"estado": "200","mensaje":"El tutorial fue actualizado correctamente"})

@csrf_exempt
def borrar_tutorial(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    id_tutorial = body["id_tutorial"]

    capturas = list(CapturaCancion.objects.filter(cancion=id_tutorial).values())

    for captura in capturas:
        nombre = captura["imagen"]
        ruta = os.getcwd() + "/app/static/uploads/" + nombre
        os.remove(ruta)

    Cancion.objects.filter(id=id_tutorial).delete()
    return JsonResponse({"estado": "200","mensaje":"El tutorial fue borrado correctamente"})

@csrf_exempt
def listar_capturas(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    id_tutorial = body["id_tutorial"]

    capturaCancion = Cancion.objects.get(id=id_tutorial)
    titulo = getattr(capturaCancion, "titulo")

    queryset = CapturaCancion.objects.filter(cancion_id=id_tutorial).order_by("orden").values()
    return JsonResponse({"estado":200,"titulo":titulo,"capturas": list(queryset)})

@csrf_exempt
def borrar_captura(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    id_captura = body["id_captura"]
    capturaCancion = CapturaCancion.objects.get(id=id_captura)
    nombre = getattr(capturaCancion, "imagen")
    CapturaCancion.objects.filter(id=id_captura).delete()
    ruta = os.getcwd() + "/app/static/uploads/" + nombre
    os.remove(ruta)
    return JsonResponse({"estado": "200","mensaje":"La captura fue borrada correctamente"})

@csrf_exempt 
def subir_captura(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)

    id_cancion = body["id_tutorial"]
    imagen_datos = body["imagen"]
    descripcion = body["descripcion"]

    formato, imgstr = imagen_datos.split(";base64,")
    ext = formato.split("/")[-1]
    data = ContentFile(base64.b64decode(imgstr))

    nombre = time.strftime("%Y%m%d-%H%M%S")+"." + ext
    ruta = os.getcwd() + "/app/static/uploads/" + nombre

    fs = FileSystemStorage()
    fs.save(ruta, data)

    CapturaCancion.objects.create(cancion=Cancion.objects.get(id=id_cancion),descripcion=descripcion,imagen=nombre,orden=1)

    return JsonResponse({"message": "Captura subida"})

def subir_imagen(request):

    id_cancion = request.POST.get("id_tutorial")
    descripcion = request.POST.get("descripcion")

    nombre = time.strftime("%Y%m%d-%H%M%S")+".png"

    ruta = os.getcwd() + "/app/static/uploads/" + nombre

    destino = open(ruta, "wb+")

    for chunk in request.FILES["imagen_local"].chunks():
        destino.write(chunk)
    destino.close()

    CapturaCancion.objects.create(cancion=Cancion.objects.get(id=id_cancion),descripcion=descripcion,imagen=nombre,orden=1)

    return JsonResponse({"message": "Imagen subida"})

@csrf_exempt
def cambiar_orden(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    id_captura = body["id_captura"]
    orden = body["orden"]
    CapturaCancion.objects.filter(id=id_captura).update(orden=orden)
    return JsonResponse({"estado": "200","mensaje":"Se cambio el orden de la imagen"})

@csrf_exempt
def cambiar_descripcion(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    id_captura = body["id_captura"]
    descripcion = body["descripcion"]
    CapturaCancion.objects.filter(id=id_captura).update(descripcion=descripcion)
    return JsonResponse({"estado": "200","mensaje":"Se cambio la descripción de la imagen"})