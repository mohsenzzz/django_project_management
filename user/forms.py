from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password','profile']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Family',
            }),
            'username': forms.TextInput(attrs={
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

            'username': {
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
        fields = ['username','password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'UserName',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            })
        }
        error_messages={
            'username': {
                'required': 'This field is required.',
            },
            'password': {
                'required': 'This field is required.',
            }
        }
