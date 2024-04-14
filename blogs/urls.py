from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/',views.logout_view, name='logout'),
    path('profile/',views.profile_view, name='profile'),
    path('add-blog/', views.add_blog, name='add_blog'),
    path('myblogs/', views.myblogs, name='myblogs'),
    path('delete-blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
