from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

# cus dashb
def customer_dashboard(request):
    return render(request, 'customer_dashboard.html')

#cus login
def customer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('customer_dashboard')
        else:
            messages.error(request, 'Invalid Customer Credentials!')

    return render(request, 'customer_login.html')  # Ensure it renders properly


def admin_login(request):
    return render(request, 'customer_login.html')  # Incorrect template


# Create your views here.
def authlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('button')
        else:
            messages.error(request, 'Username or Password Invalid !')  # <-

    return render(request,'index.html')

def authlogout(request):
    logout(request)
    messages.success(request, 'Logout Succesfully!')  # <-
    return redirect('login')

def registration(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username,password=password,email=email)
                user.save()
                return redirect('customer_login')
        else:
            messages.error(request, 'password not match')  # <-

    return render(request,'registration.html')

# Customer Dashboard
def customer_dashboard(request):
    return render(request, 'customer_dashboard.html')

# Forget Password
def forget_password(request):
    return render(request, 'forget.html')