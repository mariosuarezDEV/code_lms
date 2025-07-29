from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Modelos para nuestro perfil
from cursos.models import AlumnosInscritosModel
# Create your views here.


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "perfil.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = AlumnosInscritosModel.objects.filter(
            alumno=self.request.user)
        return context
