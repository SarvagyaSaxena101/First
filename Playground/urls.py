from django.urls import path
from . import views

urlpatterns = [
    # path('hello/',views.say_hello), # we no longer need the full version of playground/hello as the url has been included in the main file 
    # # always end path with the backslash
    path('',views.home),
    # path("hi/",views.hi),
    path('about/',views.about),
    path('services/', views.services),
    path('contact/',views.contact),
    path('home/',views.home),
    path('index/',views.index),
    path('submit/', views.submit_view, name='submit_view'),
]
