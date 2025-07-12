from django.urls import path
from .views import (
    home_view, register_view, profile_view, edit_profile,
    change_password, verify_code_view, resend_code_view, CustomLoginView
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', profile_view, name='profile'),
    path('edit/', edit_profile, name='edit_profile'),
    path('change-password/', change_password, name='change_password'),
    path('verify/', verify_code_view, name='verify_code'),
    path('resend-code/', resend_code_view, name='resend_code'),
]
