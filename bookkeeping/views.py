from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def book_keeping_index(request):
    return HttpResponse("You are at Book store .")

