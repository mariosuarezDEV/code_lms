from django.db import models
from base.models import BaseModel
from costos.models import CostosModel

# Create your models here.


class SponsorCosteoModel(BaseModel):
    costo = models.ForeignKey(
        CostosModel,
        on_delete=models.PROTECT,
        related_name="%(class)s_costo",
        verbose_name="Costo",
        null=False,
        blank=False,
        help_text="Costo asociado al patrocinador, utilizado para calcular el precio y detalles de patrocinio",
    )

    class Meta:
        verbose_name = "Patrocinador de Costeo"
        verbose_name_plural = "Patrocinadores de Costeo"
        managed = True

    def __str__(self):
        return f"Patrocinador de Costeo: {self.costo.titulo} - {self.costo.precio.amount} {self.costo.precio.currency}"
