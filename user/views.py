# from audioop import reverse
from lib2to3.fixes.fix_input import context
from django.urls import reverse
from django.contrib.auth import login
from django.http import Http404
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
        print(register_form)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user:bool = User.objects.filter(email=user_email).exists()
            if user:
                register_form.add_error('email','email already registered')
            else:
                new_user = User(first_name= register_form.cleaned_data.get('first_name'),
                                last_name= register_form.cleaned_data.get('last_name'),
                                username= register_form.cleaned_data.get('username'),
                                email=user_email,
                                email_active_code = get_random_string(72))
                new_user.set_password(register_form.cleaned_data.get('password'))
                #todo:send email active code
                print("=======================================")
                new_user.save()
                return redirect(reverse('login'))
        return render(request, 'user/register.html', {'register_form': register_form})

class ActiveUserView(View):
    def get(self, request,email_active_code):
        user = User.objects.get(email_active_code=email_active_code).first()
        if user is not None:
            if user.is_active is False:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # send active user message to user
                return redirect(reverse('login'))
            else:
                pass
                #send activated user message to user
        raise Http404




class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        print('====================login form==============================')
        return render(request, 'user/login.html',{'login_form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        print("==========================login user===================")
        for field in form:
            print("Field Error:", field.name, field.errors)
        if form.is_valid():
            print('111111111111111111111111111111')
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(username=email).first()
            if user is not None:
                 if user.is_active:
                     is_password_correct = user.check_password(password)
                     if is_password_correct:
                         login(request, user)
                         return redirect(f'home/{user.id}')
                     else:
                         form.add_error('password','email or password incorrect')
                 else:
                     form.add_error('username','user does not active')
            else:
                form.add_error('username','this username is not registered')

        print('22222222222222222222222222222222222')
        return render(request, 'user/login.html', {'login_form': form})

class UserHomeView(View):
    def get(self, request, id):
        user = User.objects.filter(id=id).first()
        return render(request, 'user/home.html',context={'user':user})



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