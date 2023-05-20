from django.urls import include, path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='home'),
    re_path(r'^capturas/(?P<id_tutorial>\d+)/$', views.capturas, name='capturas'),
    re_path(r'^generar/(?P<id_tutorial>\d+)/$', views.generar, name='generar'),
]