from django.urls import path
from . import views

urlpatterns = [
     path('registery', views.registery, name='registery'),
]