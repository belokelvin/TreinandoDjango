
from django.contrib import admin
from django.urls import path
from receitas import views

urlpatterns = [
    path('', views.home, name='login'),
]

