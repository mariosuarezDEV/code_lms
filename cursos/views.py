from django.views.generic import DetailView
from .models import CursosModel
import markdown


import markdown
from django.utils.safestring import mark_safe


class CursoDetailView(DetailView):
    model = CursosModel
    template_name = "presentacion.html"
    context_object_name = "curso"
