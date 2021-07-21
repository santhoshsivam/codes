"""Main_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from mainapp_2 import views


urlpatterns = [
        path('admin/', admin.site.urls),   
        path('form/', views.Login_page),#1
        path('form_check/', views.signin_page),#1
        path('signin/',views.signin_page),#2
        path('signin_check/', views.user_signin),#3
        path('start_test/',views.strt_test),#4
        path('index/', views.index),  # 5
        path('last_answer/', views.last_answer),
    
        
]
