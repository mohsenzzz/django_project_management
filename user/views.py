from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, LoginForm
from django.views.generic.list import ListView
from .models import User
from django.utils.crypto import get_random_string


# Create your views here.

class UserRegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'user/register.html',{'register_form':form})

    def post(self, request):
        register_form = RegisterForm(request.POST,request.FILES)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user:bool = User.objects.filter(email=user_email).exists()
            if user:
                register_form.add_error('email','email already registered')
            else:
                new_user = User(email=user_email, email_active_code = get_random_string(72))
                new_user.set_password(register_form.cleaned_data.get('password'))
                #todo:send email active code
                new_user.save()
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
    paginate_by = 1
    ordering = ['family']
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(is_active=True)
        return data
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context= context.filter(is_active=True)
    #     return context