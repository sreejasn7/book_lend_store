from django.urls import path

from . import views

urlpatterns = [
    path('', views.add_to_rent, name='add_to_rent'),
]