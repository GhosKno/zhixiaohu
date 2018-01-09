"""backend URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from backend import settings
import redis
import threading

from utils.heat import HeatQueue

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]


def on_startup(r):
    string = r.get('hot')
    if string is not None:
        # print("hot string" + string.decode("utf-8"))
        HeatQueue.from_str(string.decode("utf-8") )


def time_task():
    # print('start timer task...........')
    string = HeatQueue.to_str()
    t = r.set('hot', string)
    # print(t)
    global timer
    timer = threading.Timer(10 * 60, time_task)
    timer.start()
    # print('finish timer task...........')


r = redis.StrictRedis(host='123.206.27.172', port=6379, password='canvasRedisPassvue')
on_startup(r)
timer = threading.Timer(5 * 10, time_task)
timer.start()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)