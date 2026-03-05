"""
URL configuration for Ag project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from vasu import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.home),
    path('list/', views.product_list, name='product_list'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.http import HttpResponse

def test_host(request):
    return HttpResponse(request.get_host())

urlpatterns += [
    path('check-host/', test_host),
]


from django.http import HttpResponse
from django.conf import settings
import os

def debug_media(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'products', 'Screenshot_2025-08-06_123832.png')
    exists = os.path.exists(file_path)
    return HttpResponse(f"""
    MEDIA_ROOT = {settings.MEDIA_ROOT} <br>
    Full Path = {file_path} <br>
    Exists? = {exists}
    """)

urlpatterns += [
    path('debug-media/', debug_media),
]
