"""itblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^tinymce/', include('tinymce.urls')),
    path(r'aac/',include('aac.urls')),
    path(r'apc/',include('apc.urls')),
    path(r'arc/',include('arc.urls')),
    path(r'afc/',include('afc.urls')),
    path(r'aic/',include('aic.urls')),
    path(r'acc/',include('acc.urls')),
    path(r'',include('aic.urls')),

]

