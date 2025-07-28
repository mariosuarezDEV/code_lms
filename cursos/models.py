from django.db import models
from djmoney.models.fields import MoneyField
from base.models import BaseModel
import markdown
from django.utils.safestring import mark_safe
# Create your models here.

NIVELES = [
    ("principiante", "Principiante"),
    ("intermedio", "Intermedio"),
    ("avanzado", "Avanzado"),
]


class CategoriasModel(BaseModel):
    nombre = models.CharField(
        max_length=100, blank=False, null=False, verbose_name="Nombre de la categoría", help_text="Nombre con el que la categoría será identificada")
    descripcion = models.TextField(
        blank=True, null=True, verbose_name="Descripción de la categoría", help_text="Descripción detallada de la categoría")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        managed = True

    def __str__(self):
        return self.nombre


class CursosModel(BaseModel):
    portada = models.ImageField(
        upload_to='cursos/portadas/', blank=True, null=True)
    nombre = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="Nombre del curso", help_text="Nombre con el que el curso será identificado")
    descripcion = models.TextField(
        blank=False, null=False, verbose_name="Descripción del curso", help_text="Descripción detallada del curso")
    presentacion = models.TextField(
        blank=True, null=True, verbose_name="Presentación del curso", help_text="Presentación del curso")
    nivel = models.CharField(
        max_length=20, choices=NIVELES, default="principiante", verbose_name="Nivel del curso", help_text="Selecciona el nivel del curso")
    categoria = models.ForeignKey(CategoriasModel, on_delete=models.PROTECT,
                                  related_name="%(class)s_categoria", verbose_name="Categoría del curso")
    num_estudiantes = models.PositiveIntegerField(
        default=0, verbose_name="Número de estudiantes", help_text="Número de estudiantes inscritos en el curso")
    precio = MoneyField(max_digits=10, decimal_places=2,
                        default_currency='MXN', help_text="Precio del curso", verbose_name="Precio", blank=False, null=False)

    @property
    def presentacion_html(self):
        return mark_safe(markdown.markdown(
            self.presentacion,
            extensions=["markdown.extensions.tables"]
        ))

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        managed = True

    def __str__(self):
        return f'{self.nombre} - {self.categoria.nombre}'
