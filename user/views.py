from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, LoginForm
from django.views.generic.list import ListView
from .models import User


# Create your views here.

class UserRegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'user/register.html',{'register_form':form})

    def post(self, request):
        register_form = RegisterForm(request.POST,request.FILES)
        if register_form.is_valid():
            register_form.save()
            return redirect('register')
        return render(request, 'user/register.html', {'register_form': register_form})

class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'user/login.html',{'login_form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('home')
        return render(request, 'register.html', {'login_form': form})

class UserListView(ListView):
    model = User
    template_name = 'user/users.html'
    context_object_name = 'users'
    
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(is_active=True)
        return data
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context= context.filter(is_active=True)
    #     return context