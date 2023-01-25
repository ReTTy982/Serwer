from django.urls import path, include
from . import views

urlpatterns = [
    path('test', views.test),
    path('my_register',views.my_register),
    path('', include ("django.contrib.auth.urls")),
    path("my_login",views.my_login),
    path("populate",views.populate), # Only use once for populating database
    path("search_book",views.search_book), # Search books in branch
    path("search_my_books",views.search_my_books), # Search books of user
    ]