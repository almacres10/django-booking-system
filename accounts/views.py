from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username,
        password=password)

        if user:
            login(request, user)

            if user.role == 'admin':
                return redirect('admin_dashboard')
            return redirect('home')

        messages.error(request, 'Username atau password salah')

    return render(request, 'accounts/login.html')        

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username sudah dipakai')
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                role='customer'
            )
            login(request, user)
            return redirect('/')

    return render(request, 'accounts/register.html')


def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')