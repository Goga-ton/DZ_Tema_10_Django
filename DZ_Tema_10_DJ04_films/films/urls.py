from django.urls import path
from . import views

urlpatterns = [
    path('', views.films_stat, name='fs'),
    path('create/', views.film_create, name='fc'),

]