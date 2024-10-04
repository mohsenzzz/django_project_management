from tkinter.font import names

from django.urls import path
from . import views
urlpatterns= [
    path('register-user', views.UserRegisterView.as_view(),name='register'),
    path('login',views.UserLoginView.as_view(),name='login'),
    path('forget_password',views.ForgetPasswordView.as_view(),name='forget_password'),
    path('reset_password/<str:email_active_code>',views.ResetPasswordView.as_view(),name='reset_password'),
    path('users',views.UserListView.as_view(),name='users'),
    path('home/<int:id>',views.UserHomeView.as_view(),name='home')
]