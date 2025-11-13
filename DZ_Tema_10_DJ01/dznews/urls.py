from django.urls import path
from . import views

urlpatterns = [
    path('', views.dz_news_1, name='dzn1'),



]