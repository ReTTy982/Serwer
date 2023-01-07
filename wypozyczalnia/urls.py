from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test),
    path('my_register',views.my_register),]