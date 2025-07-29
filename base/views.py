from django.shortcuts import render
from django.urls import reverse_lazy
from allauth.account.views import LogoutView, LoginView, SignupView
from django.views.generic import TemplateView, View
from .forms import LoginForm, SignupForm
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from django.contrib import messages
# Create your views here.


class CustomLogoutView(LogoutView):
    template_name = "auth/logout.html"


class CustomLoginView(LoginView):
    template_name = "auth/login.html"
    form_class = LoginForm


class CustomSignupView(SignupView):
    template_name = "auth/signup.html"
    form_class = SignupForm


class AccountCreatedView(TemplateView):
    def get(self, request, key, *args, **kwargs):
        try:
            # Intenta obtener la confirmación con HMAC
            confirmation = EmailConfirmationHMAC.from_key(key)
            if confirmation:
                confirmation.confirm(request)  # Confirmar la cuenta
                messages.success(
                    request, 'Tu cuenta ha sido verificada correctamente.')
                # tu template
                return render(request, 'auth/confirmacion.html')
        except EmailConfirmation.DoesNotExist:
            messages.error(
                request, 'El enlace de confirmación no es válido o ha expirado.')
            return render(request, 'auth/verification.html')


class VerificationView(TemplateView):
    template_name = "auth/verification.html"

# Terminar perfil (nombre y apellido)


class CustomProfileView(SignupView):
    template_name = "auth/profile.html"
    form_class = SignupForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        # Aquí puedes agregar lógica adicional si es necesario
        return response
