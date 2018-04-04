#coding=utf-8
"""MagicMirror URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from display import views

urlpatterns = [
    #后台接口
    url(r'^admin/', admin.site.urls),
    #通信接口
    url(r'^index/', views.index),
    url(r'^frontend/', views.frontend),
    url(r'^sockets/', views.device_socket),
    url(r'^voice/', views.voice_socket),
    #空闲接口
    url(r'^get_weather_json/', views.get_weather),
    #url(r'^graphic/', views.graphic),
    #测试接口
    url(r'^testwebpage/', views.testwebpage),   #websocket测试页面
    url(r'^websockettest/', views.websockettest),   #websocket测试端口
    url(r'^sim_websocket/', views.sim_websocket),   #websocket-python模拟测试端口
]
