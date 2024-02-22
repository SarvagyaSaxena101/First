"""
URL configuration for First project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include

admin.site.site_header = "The Admin Page" # this specifies the admin login title of the div
admin.site.site_title = "Admin page" 
admin.site.index_title = "Welcome to admin portal" # this is welcome sort of messsage above all the controls of the admin web

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Playground.urls')),
    path('Playground/', include('Playground.urls'))
    # we give the url and then the include goes to the playground folder for the app so we no longer require the playground/hello in urls.py in playground
    # U can also give playground or u can include everything
]
# this is the first line that is going to be changed in the github through vscode