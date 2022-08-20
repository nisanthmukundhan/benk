from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def logintest(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('registertest')
    return render(request, 'logintest.html')


def registertest(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('registertest')
            user = User.objects.create_user(username=username, password=password)
            user.save();
            return redirect('logintest')
        else:
            messages.info(request, "password not match")

    return render(request, 'registertest.html')


def logouttest(request):
    auth.logout(request)
    return redirect('registertest')
