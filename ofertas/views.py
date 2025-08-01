from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import OfertaModel
from costos.models import CostosModel
from django.shortcuts import redirect
from django.urls import reverse_lazy
import stripe
from django.conf import settings
from decimal import Decimal
