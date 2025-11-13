from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='p1'),
    path('page2/', views.fpage1, name='p2'),
    path('page3/', views.fpage2, name='p3'),
    path('page4/', views.fpage3, name='p4'),
]