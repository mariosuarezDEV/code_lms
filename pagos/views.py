from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class GraciasPorTuPago(TemplateView):
    template_name = "mensajes/success.html"


class ErrorEnElPago(TemplateView):
    template_name = "mensajes/error.html"
