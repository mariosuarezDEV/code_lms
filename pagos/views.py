from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import stripe
from personal.models import HistorialPagos
from ofertas.models import OfertaModel
from .task import recibo_compra
from datetime import datetime
# Create your views here.


class GraciasPorTuPago(TemplateView):
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
        # Buscar el pago en el historial de pagos
        if not HistorialPagos.objects.filter(folio=datos_pago.id).exists():
            # Obtener el nombre del pago
            oferta = OfertaModel.objects.get(id=producto_id)
            HistorialPagos.objects.create(
                descripcion=f"Pago por {oferta.titulo}",
                usuario=self.request.user,
                folio=datos_pago.id,
                monto=datos_pago.amount_received / 100,  # Convertir a pesos
                estado_stripe=datos_pago.status
            )
            # Enviar el recibo de compra
            recibo_compra.delay(
                self.request.user.username,
                datetime.now(),
                oferta.descripcion,
                datos_pago.amount_received / 100,  # Convertir a pesos
                self.request.user.email
            )
        return context


class ErrorEnElPago(TemplateView):
    template_name = "mensajes/error.html"
