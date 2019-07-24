from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User


def index(request):
    return render(request, 'my-account.html')


def register(request):
    if request.method == "POST":
        print(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        # user = User.objects.create_user(email, email, password)
        return redirect('/')


