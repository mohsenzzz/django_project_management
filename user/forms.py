from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','family','userName','email','password']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
            }),
            'family': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Family',
            }),
            'userName': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'UserName',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }
            ),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            })
        }
        error_messages={

            'userName': {
                'required': 'This field is required.',
            },
            'password': {
                'required': 'This field is required.',
            },
            'email': {
                'required': 'This field is required.',
            },

        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['userName','password']
        widgets = {
            'userName': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'UserName',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            })
        }
        error_messages={
            'userName': {
                'required': 'This field is required.',
            },
            'password': {
                'required': 'This field is required.',
            }
        }
