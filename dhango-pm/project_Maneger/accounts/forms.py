from typing import Any
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext

attrs={"class":'form-control'}

class userLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(userLoginForm,self).__init__(*args,**kwargs)

    username=forms.CharField(
        label=gettext("name"),
        widget=forms.TextInput(attrs=attrs)
    )
    password=forms.CharField(
        label=gettext("password"),
        widget=forms.PasswordInput(attrs=attrs)
    )

######################################################

class userRegisterForm(UserCreationForm):
    first_name=forms.CharField(
        label=gettext("First Name "),
        widget=forms.PasswordInput(attrs=attrs)
    )
    Last_Name=forms.CharField(
        label=gettext("Last Name "),
        widget=forms.PasswordInput(attrs=attrs)
    )
    username=forms.CharField(
        label=gettext("name"),
        widget=forms.TextInput(attrs=attrs)
    )
    email=forms.EmailField(
        label=gettext("E-mail "),
        widget=forms.EmailInput(attrs=attrs)
    )
    password1=forms.CharField(
        label=gettext("password "),
        strip=False,
        widget=forms.PasswordInput(attrs=attrs)
    )
    password2=forms.CharField(
        label=gettext("Confrim password "),
        strip=False,
        widget=forms.PasswordInput(attrs=attrs),
    )
    class Meta(UserCreationForm.Meta):
        fields=('first_name','Last_Name','username','email','password1','password2')

class ProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs=attrs),
            'last_name': forms.TextInput(attrs=attrs),
            'email': forms.EmailInput(attrs=attrs),
        }

