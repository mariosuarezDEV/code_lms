from django.shortcuts import render
from allauth.account.views import LogoutView, LoginView, SignupView
from .forms import LoginForm, SignupForm
# Create your views here.


class CustomLogoutView(LogoutView):
    template_name = "auth/logout.html"


class CustomLoginView(LoginView):
    template_name = "auth/login.html"
    form_class = LoginForm


class CustomSignupView(SignupView):
    template_name = "auth/signup.html"
    form_class = SignupForm
