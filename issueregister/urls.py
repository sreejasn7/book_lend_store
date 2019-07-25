from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_rent_page, name='view_rent_page'),
    path('customer_rented/', views.RentBooksList.as_view(), name='customer_rented'),
]