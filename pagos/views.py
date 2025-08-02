from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
import stripe
from django.conf import settings

# Modelos para obtener datos
from ofertas.models import OfertaCosteoModel
from costos.models import CostosModel
from .models import HistorialPagos
from sponsors.models import SponsorCosteoModel

from .task import recibo_compra, registrar_compra
from datetime import datetime

stripe.api_key = settings.STRIPE_LIVE_SECRET_KEY


# Pagar curso
# Pagar clase
# Pagar libro
# Pagar membresía
# Pagar sponsors
class SponsorPagoView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        sponsor_costo_id = kwargs.get("id")
        sponsor = SponsorCosteoModel.objects.get(id=sponsor_costo_id)

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "mxn",
                        "unit_amount": int(sponsor.costo.precio.amount * 100),
                        "product_data": {
                            "name": sponsor.costo.titulo,
                        },
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=request.build_absolute_uri(reverse_lazy("gracias"))
            + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=request.build_absolute_uri(reverse_lazy("error_pago")),
            metadata={
                "user_id": request.user.id,
                "producto_id": sponsor.id,
                "modelo": "sponsor",
            },
        )
        return redirect(session.url)  # <-- Redirige directo a Stripe


# Pagar ofertas
class AccesoAnticipadoView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        oferta_id = kwargs.get("id")
        oferta = OfertaCosteoModel.objects.get(id=oferta_id)

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "mxn",
                        "unit_amount": int(oferta.costo.precio.amount * 100),
                        "product_data": {
                            "name": oferta.costo.titulo,
                        },
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=request.build_absolute_uri(reverse_lazy("gracias"))
            + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=request.build_absolute_uri(reverse_lazy("error_pago")),
            metadata={
                "user_id": request.user.id,
                "producto_id": oferta.id,
                "modelo": "oferta",
            },
        )
        return redirect(session.url)  # <-- Redirige directo a Stripe


class GraciasPorTuPago(LoginRequiredMixin, TemplateView):
    template_name = "mensajes/success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session_id = self.request.GET.get("session_id")
        if not session_id:
            print("No se proporcionó session_id")
            return context
        session = stripe.checkout.Session.retrieve(session_id)
        datos_pago = stripe.PaymentIntent.retrieve(session.payment_intent)

        producto_id = session.metadata.get("producto_id")
        modelo = session.metadata.get("modelo")
        # Buscar el pago en el historial de pagos
        if not HistorialPagos.objects.filter(folio=datos_pago.id).exists():
            titulo = ""
            if modelo == "oferta":
                # Obtener el nombre del pago
                objeto = OfertaCosteoModel.objects.get(id=producto_id)
            elif modelo == "sponsor":
                objeto = SponsorCosteoModel.objects.get(id=producto_id)
            else:
                objeto = None

            if objeto:
                titulo = objeto.costo.titulo
            registrar_compra.delay(
                f"Pago por {titulo}",
                self.request.user.id,
                datos_pago.id,
                datos_pago.amount_received / 100,  # Convertir a pesos
                datos_pago.status,
            )
            # Enviar el recibo de compra
            recibo_compra.delay(
                self.request.user.username,
                datetime.now(),
                titulo,
                datos_pago.amount_received / 100,  # Convertir a pesos
                self.request.user.email,
            )
        return context


class ErrorEnElPago(LoginRequiredMixin, TemplateView):
    template_name = "mensajes/error.html"
