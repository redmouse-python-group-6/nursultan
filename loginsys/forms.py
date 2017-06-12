from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import ModelForm, EmailField, forms, TextInput
from loginsys.models import UserProfile


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']


class UserCreateProfile(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', ]
        field_classes = {
            'username': UsernameField,
            'email': EmailField,
            'password1': TextInput,
            'password2': TextInput,

        }

    def __init__(self, *args, **kwargs):
        super(UserCreateProfile, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': "Имя"})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': "Email", 'type': 'email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': "Пороль"})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': "Пороль"})

