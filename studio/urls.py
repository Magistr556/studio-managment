from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('studios/', views.studio_list, name='studio_list'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('rent/<int:studio_id>/', views.rent_studio, name='rent_studio'),
    path('cancel_rent/<int:rent_id>/', views.cancel_rent, name='cancel_rent')
]