from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounts.forms import LoginForm, RegisterForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password,
            )

            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def user_logout(request):
    logout(request)
    return redirect("home")


def create_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]

            if password == password_confirmation:
                user = User.objects.create_user(username, password=password)

                login(request, user)

                return redirect("home")
            else:
                form.add_error("password", "Passwords do not match")
    else:
        form = RegisterForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/register.html", context)
