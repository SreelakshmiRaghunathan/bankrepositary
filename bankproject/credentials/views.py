from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import UserProfile
from django.shortcuts import render, redirect



# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('demo')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request,"login.html")


def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword = request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        # return redirect('/')
    return render(request,"register.html")

def demo(request):
    return render(request,"demo.html")


def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        state = request.POST['state']
        district = request.POST['district']
        branch = request.POST['branch']
        account = request.POST['account']
        materials = request.POST['materials']
        # debitcard = request.POST['debitcard']
        # creditcard = request.POST['creditcard']
        # checkbook = request.POST['checkbook']

        user= UserProfile(name=name,dob=dob,age=age,gender=gender,phone=phone,email= email,address=address,state=state,district=district,branch=branch,account=account,materials=materials)
        user.save();
        messages.info(request, "Registration successful")
        # return redirect('/')
        print()
    return render(request, "registration.html")

# def homepage(request):
#     # Add code for your homepage view here
#     return render(request, "index.html")

def logout(request):
    auth.logout(request)
    return redirect('/')