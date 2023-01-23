from django.urls import path, include
from . import views

urlpatterns = [
    path('test', views.test),
    path('my_register',views.my_register),
    path('', include ("django.contrib.auth.urls")),
    path("my_login",views.my_login),
    ]