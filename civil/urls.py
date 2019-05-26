from django.contrib import admin
from django.urls import path
from estimate.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('screen1/',screen1),
    path('screen2/',screen2),
    path('screen3/',screen3),
    path('screen4/',screen4),
    path('screen5/',screen5),
   
    path('screen3b/',screen3b),
    path('screen3c/',screen3c),
    path('screen6/',screen6),
    path('screen7/',screen7),
    path('screen8/',screen8),
    path('screen8a/',screen8a),
    path('screen9/',screen9),
    path('screen10/',screen10),
    path('screen11/',screen11),
    path('screen12/',screen12),
    path('screen13/',screen13),
    path('screen14/',screen14),
    path('admin_login/',admin_login),
    path('screen15/',screen15),
    path('screen5dem/',screen5dem),
   
]
