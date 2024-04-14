from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .middleware import auth, guest
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from .models import Article
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
@guest
def home(request):
    return render(request, 'home.html')
@guest
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(email) <= 15:
            messages.error(request, "Email should be more than 15 characters.")
            return render(request, 'login.html')

        if len(password) < 8:
            messages.error(request, "Password should be at least 8 characters.")
            return render(request, 'login.html')

        # user = authenticate(request, username=email, password=password)
        user = User.objects.get(email=email)

        if user is not None:
            if user.check_password(password):
                login(request, user)
                return redirect('dashboard') 
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
            messages.error(request, 'User alrea dy exists. Please try with another email.')
            return redirect('login')

        user = User.objects.create_user(username=fullname, email=email, password=password1)
        user.fullname = fullname 
        user.save()
        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('login')

    return render(request, 'login.html')

# @auth
# def dashboard_view(request):
#     blogs = Article.objects.order_by('-id', '-publication_date')
#     query = ""
#     if request.method == 'POST':
#         if "search" in request.POST:
#             print("search")
#             query = request.POST.get("searchquery","")
#             print("query",query)
#             blogs = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-id','-publication_date')

#     return render(request, 'dashboard.html', {'blogs': blogs})

def dashboard_view(request):
    blogs_list = Article.objects.order_by('-id', '-publication_date')
    query = ""

    if request.method == 'POST':
        if "search" in request.POST:
            query = request.POST.get("searchquery", "")
            blogs_list = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-id', '-publication_date')

    paginator = Paginator(blogs_list, 6)  # Adjust the number of blogs per page as needed
    page = request.GET.get('page')

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'dashboard.html', {'blogs': blogs})


def logout_view(request):
    logout(request)
    return redirect('login')

@auth
def profile_view(request):
    user = request.user  # Get the logged-in user

    if request.method == 'POST':
        # Process form data for updating profile (if needed)
        # Example: user.first_name = request.POST['first_name']
        # Save user data: user.save()

        messages.success(request, 'Profile updated successfully.')

    return render(request, 'profile.html', {'user': user})

@auth
# def add_blog(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         image = request.FILES.get('image')

#         if not title or not content or not image:
#             messages.error(request, 'Please fill in all required fields.')
#             return redirect('dashboard')

#         try:
#             article = Article.objects.create(
#                 title=title,
#                 content=content,
#                 image=image,
#                 added_by=request.user  # Set the added_by field to the current user
#             )
#             messages.success(request, 'Blog added successfully!')
#             print("article___",article)
#         except Exception as e:
#             messages.error(request, f'Error adding blog: {str(e)}')

#     return redirect('dashboard')
@auth
def add_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        if not title or not content or not image:
            messages.error(request, 'Please fill in all required fields.')
            return redirect('dashboard')

        try:
            article = Article.objects.create(
                title=title,
                content=content,
                image=image,
                added_by=request.user
            )
            messages.success(request, 'Blog added successfully!')
            return JsonResponse({'success': True})  # Return JSON response for success
        except Exception as e:
            messages.error(request, f'Error adding blog: {str(e)}')
            return JsonResponse({'success': False, 'error': str(e)})  # Return JSON response for error

    return redirect('dashboard')

@guest
def signup_view(request):
    print("signup accessed")
    return render(request, 'signup.html')

# @auth
# def myblogs(request):
#     blogs = Article.objects.order_by('-id', '-publication_date').filter(added_by=request.user)
#     query = ""
#     if request.method == 'POST':
#         if "search" in request.POST:
#             print("search")
#             query = request.POST.get("searchquery","")
#             print("query",query)
#             # blogs = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-id','-publication_date')
#             blogs = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query), added_by=request.user).order_by('-id', '-publication_date')

#     return render(request, 'myblogs.html', {'blogs': blogs})

@auth
def myblogs(request):
    blogs_list = Article.objects.filter(added_by=request.user).order_by('-id', '-publication_date')

    blogs_per_page = 6  

    paginator = Paginator(blogs_list, blogs_per_page)

    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    query = ""
    if request.method == 'POST':
        if "search" in request.POST:
            query = request.POST.get("searchquery", "")
            blogs_list = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query), added_by=request.user).order_by('-id', '-publication_date')
            paginator = Paginator(blogs_list, blogs_per_page)

            page = request.GET.get('page')
            try:
                blogs = paginator.page(page)
            except PageNotAnInteger:
                blogs = paginator.page(1)
            except EmptyPage:
                blogs = paginator.page(paginator.num_pages)

    return render(request, 'myblogs.html', {'blogs': blogs})


@auth
def delete_blog(request, blog_id):
    blog = get_object_or_404(Article, id=blog_id)

    # Check if the logged-in user is the author of the blog
    if request.user == blog.added_by:
        blog.delete()
        return redirect('myblogs')
    else:
        # Return some error response or redirect as needed
        return redirect('myblogs')  # Redirect for now

@auth
def edit_blog(request, blog_id):
    if request.method == 'POST':
        blog = Article.objects.get(pk=blog_id)
        blog.title = request.POST.get('title')
        blog.content = request.POST.get('content')
        if 'image' in request.FILES:
            blog.image = request.FILES['image']
        blog.save()
        return redirect('myblogs')
    else:
        # Handle GET request or other cases as needed
        pass