from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import EmployeeProfile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_type']
class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = ['resume', 'skills']
