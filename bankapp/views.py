from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from bankapp.models import Register, District, Branch, Account
# Create your views here.



def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        mail = request.POST.get('mail')
        address = request.POST.get('address')
        regi = Register(name=name, dob=dob, age=age, gender=gender, phone=phone, mail=mail, address=address)
        regi.save()
        messages.info(request, "accepted")

    return render(request, 'register.html')


def registerform(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        paswordd = request.POST['passwordd']
        if password == paswordd:
            user = User.objects.create_user(username=username, password=password)
            user.save();
            return redirect('login/')


        else:
            print("password is not match")
            return redirect('registerform')

    return render(request, 'registerform.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            messages.info(request, 'invalid')
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def districtfull(request):
    obj = District.objects.all()
    return render(request, 'home.html', {'district': obj})


def demo1(request):
    return render(request, 'navbar.html')


def navbar(request):
    return render(request, 'navbar1.html')


def districtdetail(request, d_slug):
    d = District.objects.get(slug=d_slug)
    return render(request, 'district.html', {'d': d})


def branchdetail(request):
    b = Branch.objects.all()
    return render(request, 'register.html', {'b': b})


def accountdetail(request, a_slug):
    a = Account.objects.get(slug=a_slug)
    return render(request, 'register.html', {'a': a})


def meterialdetail(request, m_slug):
    mm = Account.objects.get(slug=m_slug)
    return render(request, 'register.html', {'mm': mm})


def meterialdetails(request, ):
    ms = Account.objects.all
    return render(request, 'register.html', {'ms': ms})
