from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "perfil.html"
