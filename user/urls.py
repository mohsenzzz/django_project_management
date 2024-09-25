from tkinter.font import names

from django.urls import path
from . import views
urlpatterns= [
    path('register-user', views.UserRegisterView.as_view(),name='register'),
]