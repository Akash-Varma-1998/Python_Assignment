from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
# from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
# from .models import Employee, Products

# Create your views here.
def home(request):
    return render(request, 'index.html')