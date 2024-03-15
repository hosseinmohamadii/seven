from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import User, Critic
from .forms import CriticForm, RegisterForm, LoginForm
from django.contrib import messages

def register(request):
    if request.user.is_authenticated:
        messages.error(request,'You have already registered','error')
        return redirect('logout')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                )
                messages.success(request,'Your information has been saved successfuly','success')
                login(request, user)
                return redirect('all-c')
            else:
                return render(request, 'create.html', {'form':form})
        else:
            return render(request, 'create.html', {'form':RegisterForm()})

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('logout')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password']
                )
                messages.success(request,'Your information has been saved successfully','success')
                if user:
                    login(request, user)
                    return redirect('all-c')
                else:
                    return render(request, 'create.html', {'form':form})

            else:
                return render(request, 'create.html', {'form':form})
        else:
            return render(request, 'create.html', {'form':LoginForm()})

def userlogout(request):
    logout(request)
    messages.success(request,'logout successfully','success')
    return redirect('login')

def new(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CriticForm(request.POST)
            if form.is_valid():
                user = User.objects.get(id=request.user.id)
                c = Critic.objects.create(
                    title=form.cleaned_data['title'],
                    text=form.cleaned_data['text'],
                    creator=user
                )
                messages.success(request,'Your review has been successfully registered','success')
                return redirect('login')
            else:
                return render(request, 'create.html', {'form':form})
        else:
            return render(request, 'create.html', {'form':CriticForm()})
    else:
        return redirect('login')
    
def listc(request):
    cqs = Critic.objects.all()
    return render(request, 'list.html', {'objs':cqs})
                                                  
        