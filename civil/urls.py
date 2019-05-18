from django.contrib import admin
from django.urls import path
from estimate.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home),
    path('screen2/',screen2),
    path('screen3/',screen3),
    path('screen4/',screen4),
    path('screen5/',screen5),
]
