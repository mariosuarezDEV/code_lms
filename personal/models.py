from django.contrib.auth.models import AbstractUser
from django.db import models
import os
from PIL import Image
from djmoney.models.fields import MoneyField


class CustomUser(AbstractUser):
    foto_perfil = models.ImageField(
        upload_to='perfil/', blank=True, null=True, verbose_name="Foto de perfil",
        help_text="Sube una foto de perfil")

    biografia = models.TextField(
        blank=True, null=True, verbose_name="Biografia", help_text="Escribe una biografía breve")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.foto_perfil:
            ruta = self.foto_perfil.path
            try:
                with Image.open(ruta) as img:
                    # Redimensionar si es muy grande (opcional)
                    max_size = (460, 460)
                    img.thumbnail(max_size)

                    # Convertir a RGB (necesario si suben PNG con transparencia)
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")

                    # Comprimir y sobrescribir imagen original
                    img.save(ruta, format='JPEG', quality=80)

            except Exception as e:
                print(f"Error al procesar la imagen: {e}")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class HistorialPagos(models.Model):
    usuario = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='historial_pagos')
    folio = models.CharField(max_length=255, unique=True, verbose_name="Folio del pago",
                             help_text="Folio único del pago en Stripe")
    monto = MoneyField(
        max_digits=10, decimal_places=2, default_currency='MXN', verbose_name="Monto del pago")
    fecha = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha del pago", help_text="Fecha y hora en que se realizó el pago")
    estado_stripe = models.CharField(
        max_length=50, verbose_name="Estado del pago en Stripe", help_text="Estado del pago según Stripe")
    descripcion = models.CharField(
        max_length=255, verbose_name="Descripción del pago", help_text="Descripción breve del pago")

    class Meta:
        verbose_name = "Historial de Pagos"
        verbose_name_plural = "Historial de Pagos"
        ordering = ['-fecha']
        managed = True

    def __str__(self):
        return f'{self.usuario} - {self.folio} - {self.monto} - {self.fecha} - {self.estado_stripe}'
