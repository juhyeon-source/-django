from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def home(request):
    return render(request, 'accounts/home.html')

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("accounts:home")
    else:
        form = AuthenticationForm()
    context = {'form' : form }
    return render(request, 'accounts/login.html', context)