from django.urls import path, include
from .views import CustomLogoutView, CustomLoginView, CustomSignupView


urlpatterns = [
    path("salir/", CustomLogoutView.as_view(), name="account_logout"),
    path("entrar/", CustomLoginView.as_view(), name="account_login"),
    path("registrar/", CustomSignupView.as_view(), name="account_signup"),
]
