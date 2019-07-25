from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_rent_page, name='view_rent_page'),
]