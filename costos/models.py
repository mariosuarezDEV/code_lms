from django.db import models
from base.models import BaseModel
from djmoney.models.fields import MoneyField

# Tabla de costos y precios de la plataforma


class CostosModel(BaseModel):
    titulo = models.CharField(
        max_length=50,
        verbose_name="Título del Costo",
        help_text="Título descriptivo del costo",
        blank=False,
        null=False,
    )
    descripcion = models.TextField(
        verbose_name="Descripción del Costo",
        help_text="Descripción detallada del costo",
        blank=True,
        null=True,
    )
    precio = MoneyField(
        max_digits=10,
        decimal_places=2,
        default_currency="MXN",
        verbose_name="Precio",
        help_text="Precio del costo en la moneda seleccionada",
    )

    class Meta:
        verbose_name = "Costo"
        verbose_name_plural = "Costos"
        managed = True

    def __str__(self):
        return self.titulo
