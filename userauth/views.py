# Create your views here.
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
 
@login_required
def homepage(request):
    return render(request, "home.html", {})
@csrf_exempt
def signuppage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "SignUp successful!")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password = password)
            login(request, user)
            obj=users(username=username,password=password)
            obj.save()
            return redirect('homepage')

    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
# def signup(request):
#     form = CreateUserForm()

#     if request.method =="POST":
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Account Created. Please Login.')
#         else:
#             messages.warning(request, 'Something went wrong. Please try again')
#     return render(request, 'signup.html', {'form':form})
@csrf_exempt
def signinpage(request):
    if request.method == "POST":
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('homepage')

        else:
            messages.warning(request, "Wrong Username or Password. Try Again")
    return render(request, 'signin.html')
@csrf_exempt
def logoutuser(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('signinpage')
