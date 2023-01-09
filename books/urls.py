from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('insert', views.insert_books, name='insert_books')
]
