from datetime import datetime
import markdown
from django.core.mail import EmailMultiAlternatives
from celery import shared_task
from .models import HistorialPagos
from django.contrib.auth import get_user_model

User = get_user_model()


@shared_task
def recibo_compra(nombre, fecha_compra, descripcion, monto, cliente):
    subject = "Recibo de compra - Gracias por tu compra"
    from_email = "lmcervantessuarez@gmail.com"
    # Cambia por el email real del cliente
    to = [cliente]

    # Formatear la fecha en formato legible
    fecha_formateada = fecha_compra.strftime("%d/%m/%Y %H:%M")

    markdown_content = f"""
# Recibo de Compra

Hola, **{nombre}**!

Gracias por tu compra realizada el **{fecha_formateada}**.

---

### Detalles de la compra

- **Descripción:** {descripcion}
- **Monto:** ${monto:.2f} MXN

---

Si tienes alguna duda, no dudes en contactarnos.

¡Gracias por preferirnos!

[Visita nuestra web](https://lmsuarez.pythonanywhere.com)
    """

    html_content = markdown.markdown(markdown_content)
    text_content = markdown_content  # Texto plano con markdown sin procesar

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@shared_task
def registrar_compra(descripcion, usuario, folio, monto, estado_stripe):
    usuario = User.objects.get(id=usuario)
    HistorialPagos.objects.create(
        usuario=usuario,
        folio=folio,
        monto=monto,
        fecha=datetime.now(),
        estado_stripe=estado_stripe,
        descripcion=descripcion,
    )
