from django.urls import include, path, re_path
from . import views

urlpatterns = [
    re_path(r'^tutoriales/$', views.listar_tutoriales, name='listar_tutoriales'),
    re_path(r'^tutoriales/cargar$', views.cargar_tutorial, name='cargar_tutorial'),
    re_path(r'^tutoriales/agregar$', views.agregar_tutorial, name='agregar_tutorial'),
    re_path(r'^tutoriales/editar$', views.editar_tutorial, name='editar_tutorial'),
    re_path(r'^tutoriales/borrar$', views.borrar_tutorial, name='borrar_tutorial'),
    re_path(r'^capturas/$', views.listar_capturas, name='listar_capturas'),
    re_path(r'^capturas/subir$', views.subir_captura, name='subir_captura'),
    re_path(r'^capturas/borrar$', views.borrar_captura, name='borrar_captura'),
    re_path(r'^capturas/cambiarOrden$', views.cambiar_orden, name='cambiar_orden'),
    re_path(r'^capturas/cambiarDescripcion$', views.cambiar_descripcion, name='cambiar_descripcion'),
]