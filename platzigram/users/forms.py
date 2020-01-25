

# Django
from django import forms
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
        username = forms.CharField(
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control',
                'required': True
                }
        )
    )
        password = forms.CharField(
            min_length=6,
            max_length=70,
            widget=forms.PasswordInput(
                attrs={
                    'placeholder': 'Password',
                    'class': 'form-control',
                    'required': True
                }
            )
        )
        password_confirmation = forms.CharField(
            min_length=6,
            max_length=70,
            widget = forms.PasswordInput(
                attrs={
                    'placeholder': 'Password Confirmation',
                    'class': 'form-control',
                    'required': True
                }
            )
        )

        first_name = forms.CharField(
            min_length=3,
            max_length=50,
            widget=forms.TextInput(
                attrs={
                    'placeholder':'First name',
                    'class': 'form-control',
                    'required': True
                    }
                )
            )
        last_name = forms.CharField(
            min_length=3,
            max_length=50,
            widget=forms.TextInput(
                attrs={
                    'placeholder': 'Last name',
                    'class': 'form-control',
                    'required': True
                    }
            )
        )

        email = forms.CharField(
            min_length=6,
            max_length=70,
            widget=forms.EmailInput(
                attrs={
                    "placeholder": "email",
                    "class": "form-control",
                    'required': True
                }
            )
        )
        def clean_username(self):
            username = self.cleaned_data['username']
            username_taken = User.objects.filter(username = username).exists()
            if username_taken:
                raise forms.ValidationError('Username is already taken')
            return username

        def clean(self):
            data = super().clean()
            password = data['password']
            password_confirmation = data['password_confirmation']
            if password != password_confirmation:
                raise forms.ValidationError('password do not match')
            return data

        def save(self):
                data = self.cleaned_data
                data.pop('password_confirmation')

                user = User.objects.create_user(**data)
                profile = Profile(user=user)
                profile.save()
