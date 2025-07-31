from django.views.generic import TemplateView
from cursos.models import CursosModel
from django.shortcuts import redirect


class LandingPageView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cursos"] = CursosModel.objects.all()[:3]
        return context


class PresalePageView(TemplateView):
    template_name = "lanzamiento.html"
