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
    path("author",views.author),
    path('book_copies',views.book_copies),
    path('books',views.books),
    path('authors',views.authors),
    path('issue_book',views.issue_book),
    path('library_user',views.library_user),
    ]