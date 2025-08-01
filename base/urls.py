from django.urls import path, include
from .views import (
    CustomLogoutView,
    CustomLoginView,
    CustomSignupView,
    AccountCreatedView,
    VerificationView,
)


urlpatterns = [
    path("salir/", CustomLogoutView.as_view(), name="account_logout"),
    path("entrar/", CustomLoginView.as_view(), name="account_login"),
    path("registrar/", CustomSignupView.as_view(), name="account_signup"),
    path(
        "confirmacion/<key>/",
        AccountCreatedView.as_view(),
        name="account_confirm_email",
    ),
    path(
        "verificacion/",
        VerificationView.as_view(),
        name="account_email_verification_sent",
    ),
]
