from django.urls import path
from . import views

urlpatterns = [
    path('', views.exchanger, name='index'),
]
