"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views,testdb

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.login),
    path('index/', views.index),
    path('runoob/', views.runoob),
    path('login/', views.login),
    path('testdb/', testdb.testdb),
    path('draft/', views.draft),
    path('border/', views.border),
    path('test/', views.test),
    path('liushuideng/', views.liushuideng),
    path('img/', views.img),
    path('button/', views.button),
    path('text/', views.text),
    path('User/',include('User.urls')),
]

# 在开发环境中，添加静态文件URL配置
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)