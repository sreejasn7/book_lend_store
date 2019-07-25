from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from bookkeeping.models import BookChargeSheet


def index(request):
    # book_types= BookChargeSheet.objects.all()
    return render(request, 'index.html')
    # return redirect('/store')


def register(request):
    if request.method == "POST":
        print(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(email, email, password)
        return render(request, 'messages.html')
    else:
        return render(request, 'my-account.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            print("session set for user")
            return redirect('/store/')
    else:
        print("Not logged in")
        return redirect('/')


def logout_user(request):
    logout(request)
    print("User logged out")
    return redirect('/')
