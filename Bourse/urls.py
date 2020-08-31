"""Bourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,re_path,include
from registeration import views as v
from web.views import add_buy,add_sell,property_table,add_deposit,deposit_table
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('register/', v.register , name='register'),
    path('resetpassword/', v.reset_pasword , name='reset password'),
    path('login/', v.Login , name='login'),
    #re_path(r'test/(\d{3})', test , name='test'),
    path('logout/', v.Logout , name='logout'),
    path('', v.index , name='index'),
    path('add_buy/', add_buy , name='add buy'),
    path('add_sell/', add_sell , name='add sell'),
    path('add_deposit/', add_deposit , name='add deposit'),
    re_path(r'^stats/properties/(\d*)$', property_table , name='property table'),
    re_path(r'^stats/deposits/(\d*)$', deposit_table , name='deposite table'),    
    re_path(r'^web/',include("web.urls"),name='Web')
]
