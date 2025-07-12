from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'full_name', 'bio', 'location']
