from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'), 
    path('calculate', views.calculate), 
    path('detect', views.detect), 
]