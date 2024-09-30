from tkinter.font import names

from django.urls import path
from . import views
urlpatterns= [
    path('register-user', views.UserRegisterView.as_view(),name='register'),
    path('login',views.UserLoginView.as_view(),name='login'),
    path('users',views.UserListView.as_view(),name='users'),
    path('home/<int:id>',views.UserHomeView.as_view(),name='home')
]