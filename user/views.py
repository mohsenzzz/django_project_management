from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, LoginForm


# Create your views here.

class UserRegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'user/register.html',{'register_form':form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('register')
        return render(request, 'user/register.html', {'register_form': register_form})

class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'user/login.html',{'login_form':form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            return redirect('home')
        return render(request, 'register.html', {'register_form': login_form})