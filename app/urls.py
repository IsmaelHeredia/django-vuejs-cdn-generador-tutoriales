from django.urls import include, path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='home'),
    re_path(r'^capturas/(?P<id_tutorial>\d+)/$', views.capturas, name='capturas'),
    re_path(r'^generar/(?P<id_tutorial>\d+)/$', views.generar, name='generar'),
    re_path(r'^estadisticas/$', views.estadisticas, name='estadisticas'),
    re_path(r'^about/$', views.about, name='about'),
]