from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from .middleware import auth, guest
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
 
# Create your views here.
@guest
def home(request):
    return render(request, 'home.html')
@guest
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Custom validation checks
        if len(email) <= 15:
            messages.error(request, "Email should be more than 15 characters.")
            return render(request, 'login.html')

        if len(password) < 8:
            messages.error(request, "Password should be at least 8 characters.")
            return render(request, 'login.html')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            # messages.success(request, "User logged in successfully")
            return redirect('dashboard')  # Redirect to dashboard or any other page
        else:
            messages.error(request, "Login failed. User not found or incorrect password.")
            return render(request, 'login.html')

    return render(request, 'login.html')

@guest
def register_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'User already exists. Please try with another email.')
            return redirect('login')

        user = User.objects.create_user(username=fullname, email=email, password=password1)
        user.fullname = fullname 
        user.save()
        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('login')

    return render(request, 'login.html')

@auth
def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

