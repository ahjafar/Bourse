from django.urls import path,include
from . import views
from django.urls import path,re_path,include

urlpatterns = [
    re_path(r'^add_buy/$',views.add_buy),
    re_path(r'^add_sell/$',views.add_sell)

]