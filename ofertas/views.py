from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import OfertaModel
from django.shortcuts import redirect
from django.urls import reverse_lazy
import stripe
from django.conf import settings
from decimal import Decimal
stripe.api_key = settings.STRIPE_SECRET_KEY


class AccesoAnticipadoView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        oferta_id = kwargs.get("id")
        oferta = OfertaModel.objects.get(id=oferta_id)

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "mxn",
                        "unit_amount": int(oferta.precio.amount * 100),
                        "product_data": {
                            "name": oferta.titulo,
                        },
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=request.build_absolute_uri(reverse_lazy("gracias")),
            cancel_url=request.build_absolute_uri(reverse_lazy("error_pago")),
        )
        return redirect(session.url)  # <-- Redirige directo a Stripe
