from django.views.generic import DetailView, ListView
from .models import CursosModel
import markdown


import markdown
from django.utils.safestring import mark_safe


class CursoListView(ListView):
    model = CursosModel
    template_name = "lista.html"
    context_object_name = "cursos"


class CursoDetailView(DetailView):
    model = CursosModel
    template_name = "presentacion.html"
    context_object_name = "curso"
