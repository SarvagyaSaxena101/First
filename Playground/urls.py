from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('service1/', views.service1),
    path('service2/', views.service2),
    path('contact/', views.contact),
    path('home/', views.home),
    path('index/', views.index),
    path('submit/', views.submit_view, name='submit_view'),
    path('service/', views.generate_qr, name='generate_qr'),
]
