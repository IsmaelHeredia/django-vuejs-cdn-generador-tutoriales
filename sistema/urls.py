from django.contrib import admin
from django.urls import path,re_path, include
from api import urls as api_urls
from app import urls as app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    re_path(r'^', include(app_urls)),
]
