from django.urls import path

from . import views

urlpatterns = [
    path('', views.book_keeping_index, name='book_keeping_index'),
]