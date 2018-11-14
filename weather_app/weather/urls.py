from django.urls import path
from . import views

urlpatterns = [
    path('avg-temp', views.avg_temp, name='avg-temp'),
]
