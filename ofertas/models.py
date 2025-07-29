from django.db import models
from djmoney.models.fields import MoneyField
from base.models import BaseModel
# Create your models here.


class OfertaModel(BaseModel):
    titulo = models.CharField(
        max_length=255, verbose_name="Título de la oferta", help_text="Titulo que será mostrado en la pasarela de pago", null=False, blank=False)
    descripcion = models.TextField(
        verbose_name="Descripción de la oferta", help_text="Descripción que será mostrada en la pasarela de pago", null=False, blank=False)
    precio = MoneyField(max_digits=10, decimal_places=2, default_currency='MXN',
                        help_text="Precio del curso", verbose_name="Precio", blank=False, null=False)

    class Meta:
        verbose_name = "Oferta"
        verbose_name_plural = "Ofertas"
        managed = True

    def __str__(self):
        return f'{self.titulo} - {self.precio}'
