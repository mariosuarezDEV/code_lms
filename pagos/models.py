from django.db import models
from django.conf import settings
from base.models import BaseModel
from django.contrib.auth import get_user_model
from djmoney.models.fields import MoneyField

User = get_user_model()

# Create your models here.


class HistorialPagos(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="historial_pagos"
    )
    folio = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Folio del pago",
        help_text="Folio único del pago en Stripe",
    )
    monto = MoneyField(
        max_digits=10,
        decimal_places=2,
        default_currency="MXN",
        verbose_name="Monto del pago",
    )
    fecha = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha del pago",
        help_text="Fecha y hora en que se realizó el pago",
    )
    estado_stripe = models.CharField(
        max_length=50,
        verbose_name="Estado del pago en Stripe",
        help_text="Estado del pago según Stripe",
    )
    descripcion = models.CharField(
        max_length=255,
        verbose_name="Descripción del pago",
        help_text="Descripción breve del pago",
    )

    class Meta:
        verbose_name = "Historial de Pagos"
        verbose_name_plural = "Historial de Pagos"
        ordering = ["-fecha"]
        managed = True

    def __str__(self):
        return f"{self.usuario} - {self.folio} - {self.monto} - {self.fecha} - {self.estado_stripe}"
