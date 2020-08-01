from django.urls import path,include
from . import views
from django.urls import path,re_path,include

urlpatterns = [
    re_path(r'^salam/$',views.test)
]