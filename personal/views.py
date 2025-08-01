from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import CustomUserForm
from .models import CustomUser

# Modelos para nuestro perfil
from pagos.models import HistorialPagos

# Modelos para nuestro perfil
from cursos.models import AlumnosInscritosModel

# Create your views here.


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "perfil.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cursos"] = AlumnosInscritosModel.objects.filter(
            alumno=self.request.user
        )
        context["pagos"] = HistorialPagos.objects.filter(usuario=self.request.user)
        return context


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = "actualizar.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy("account_profile")

    def form_valid(self, form):
        # Esto se encarga automáticamente de manejar request.FILES
        return super().form_valid(form)
