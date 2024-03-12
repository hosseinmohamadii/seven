from django import forms
from .models import Critic, User

class CriticForm(forms.ModelForm):
    class Meta:
        model = Critic
        fields = ['title', 'text']
    
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']