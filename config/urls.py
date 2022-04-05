"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('intro/', include('intro.urls')),
    path('draw/', include('draw.urls')),
    path('isitnewyear/', include('newyear.urls')),
    path('mem/', include('mem.urls')),
    path('link/', include('linkapp.urls')),
    path('formapp2/', include('formapp.urls')),
    path('calculator/', include('calculator.urls')),
    path('task/', include('taskapp.urls')),
    path('formapp2/', include('formapp2.urls')),
    path('viewapp/', include('viewapp.urls')),
    path('task2/', include('taskapp2.urls')),
    path('auth/', include('authapp.urls')),
]
