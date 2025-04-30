from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(request):
    return render(request, "users/home.html")  # Fixed slash direction for path

def logout_view(request):
    logout(request)
    return redirect("/")