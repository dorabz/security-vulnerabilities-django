from django.urls import path,include

from .import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path("ba",views.ba,name="Broken Access Control"),
    path("ba_lab",views.ba_lab,name="Broken Access Control Lab"),
    path("data_exp",views.data_exp,name="data_exp"),
    path("data_exp_lab",views.data_exp_lab,name="data_exp_lab"),
    path("robots.txt",views.robots,name="robots.txt"),
]
