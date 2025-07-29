from django.contrib.auth.models import AbstractUser
from django.db import models
import os
from PIL import Image


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
    pass
