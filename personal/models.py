from django.contrib.auth.models import AbstractUser
from django.db import models
import os
from PIL import Image
import markdown
from django.utils.safestring import mark_safe
from djmoney.models.fields import MoneyField


class CustomUser(AbstractUser):
    foto_perfil = models.ImageField(
        upload_to="perfil/",
        blank=True,
        null=True,
        verbose_name="Foto de perfil",
        help_text="Sube una foto de perfil",
    )

    biografia = models.TextField(
        blank=True,
        null=True,
        verbose_name="Biografia",
        help_text="Escribe una biografía breve",
    )

    @property
    def biografia_html(self):
        return mark_safe(
            markdown.markdown(self.biografia, extensions=["markdown.extensions.tables"])
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.foto_perfil:
            ruta = self.foto_perfil.path
            try:
                with Image.open(ruta) as img:
                    # Redimensionar si es muy grande
                    max_size = (460, 460)
                    img.thumbnail(max_size)

                    # Comprimir y sobrescribir imagen original
                    img.save(ruta, format="JPEG", quality=80)

            except Exception as e:
                print(f"Error al procesar la imagen: {e}")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
