from django import forms
from .models import Critic, User

class CriticForm(forms.ModelForm):
    class Meta:
        model = Critic
        fields = ['title', 'text']
    
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)