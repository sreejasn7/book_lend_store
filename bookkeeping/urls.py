from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.book_keeping_index, name='book_keeping_index'),
    path('<int:book_type_id>/', views.book_keeping_index, name='book_keeping_index'),
    path('detail/<int:book_id>/', views.book_detail, name='detail'),
    path('rent/', views.rent_books, name='rent'),
    path('book_types/', views.get_book_charge_sheet, name='book_types'),
    path('calculate_rent/', views.get_book_rent_price, name='calculate_rent'),

]
urlpatterns += staticfiles_urlpatterns()
