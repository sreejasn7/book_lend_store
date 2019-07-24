from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def add_to_rent(request):
    return HttpResponse("You are at Book store .")

