from django.shortcuts import render
from django.http import HttpResponse


def view_rent_page(request):
    return render(request, 'wishlist.html')

