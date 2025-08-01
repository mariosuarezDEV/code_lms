from django.db import models
from base.models import BaseModel
from costos.models import CostosModel

# Create your models here.


class OfertaCosteoModel(BaseModel):
    costo = models.ForeignKey(
        CostosModel,
        on_delete=models.PROTECT,
        related_name="%(class)s_costo",
        verbose_name="Costo",
        null=False,
        blank=False,
        help_text="Costo asociado a la oferta, utilizado para calcular el precio y detalles de venta",
    )

    class Meta:
        verbose_name = "Oferta de Costeo"
        verbose_name_plural = "Ofertas de Costeo"
        managed = True

    def __str__(self):
        return f"Oferta de Costeo: {self.costo.titulo} - {self.costo.precio.amount} {self.costo.precio.currency}"
