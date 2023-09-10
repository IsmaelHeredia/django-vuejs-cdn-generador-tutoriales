from django.urls import include, path, re_path
from . import views

urlpatterns = [
    re_path(r'^dificultades/$', views.listar_dificultades, name='listar_dificultades'),
    re_path(r'^generos/$', views.listar_generos, name='listar_generos'),

    re_path(r'^tutoriales/$', views.listar_tutoriales, name='listar_tutoriales'),
    re_path(r'^tutoriales/cargar$', views.cargar_tutorial, name='cargar_tutorial'),
    re_path(r'^tutoriales/agregar$', views.agregar_tutorial, name='agregar_tutorial'),
    re_path(r'^tutoriales/editar$', views.editar_tutorial, name='editar_tutorial'),
    re_path(r'^tutoriales/borrar$', views.borrar_tutorial, name='borrar_tutorial'),

    re_path(r'^tutoriales_filtro_titulo$', views.listar_tutoriales_filtro_titulo, name='listar_tutoriales_filtro_titulo'),
    re_path(r'^tutoriales_filtro_afinacion$', views.listar_tutoriales_filtro_afinacion, name='listar_tutoriales_filtro_afinacion'),
    re_path(r'^tutoriales_filtro_dificultad$', views.listar_tutoriales_filtro_dificultad, name='listar_tutoriales_filtro_dificultad'),
    re_path(r'^tutoriales_filtro_genero$', views.listar_tutoriales_filtro_genero, name='listar_tutoriales_filtro_genero'),

    re_path(r'^capturas/$', views.listar_capturas, name='listar_capturas'),
    re_path(r'^capturas/subir$', views.subir_captura, name='subir_captura'),
    re_path(r'^capturas/subirImagen$', views.subir_imagen, name='subir_imagen'),
    re_path(r'^capturas/borrar$', views.borrar_captura, name='borrar_captura'),
    re_path(r'^capturas/cambiarOrden$', views.cambiar_orden, name='cambiar_orden'),
    re_path(r'^capturas/cambiarDescripcion$', views.cambiar_descripcion, name='cambiar_descripcion'),
]