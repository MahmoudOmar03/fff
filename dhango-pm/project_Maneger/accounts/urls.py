from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from . import forms
from accounts.views import RegisterView , edit_profile

urlpatterns = [
    path("login/",LoginView.as_view(authentication_form=forms.userLoginForm), name="login"),
    path("register/",RegisterView.as_view(), name="register"),
    path("profile/",edit_profile, name="profile"),
    path("",include("django.contrib.auth.urls")),
]