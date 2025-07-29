from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
import os
from django.core.files.base import ContentFile
from io import BytesIO


class CustomUser(AbstractUser):
    foto_perfil = models.ImageField(
        upload_to='perfil/', blank=True, null=True, verbose_name="Foto de perfil",
        help_text="Sube una foto de perfil")

    biografia = models.TextField(
        blank=True, null=True, verbose_name="Biografia", help_text="Escribe una biografía breve")

    def save(self, *args, **kwargs):
        # Guardar temporalmente la imagen original
        original = self.foto_perfil

        super().save(*args, **kwargs)

        if original:
            ruta_original = self.foto_perfil.path
            nombre_original = os.path.basename(ruta_original)
            nombre_base, _ = os.path.splitext(nombre_original)
            ruta_webp = os.path.join(os.path.dirname(
                ruta_original), f"{nombre_base}.webp")

            try:
                # Abrir imagen original
                with Image.open(ruta_original) as img:
                    # Convertir a RGB si es necesario
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")

                    # Redimensionar si es muy grande
                    max_size = (500, 500)
                    img.thumbnail(max_size)

                    # Guardar imagen en buffer como webp
                    buffer = BytesIO()
                    img.save(buffer, format="WEBP", quality=80)
                    buffer.seek(0)

                    # Eliminar archivo original
                    if os.path.exists(ruta_original):
                        os.remove(ruta_original)

                    # Guardar archivo webp en el campo
                    self.foto_perfil.save(
                        f"{nombre_base}.webp", ContentFile(buffer.read()), save=False)
                    buffer.close()

                    # Guardar el modelo con el nuevo archivo
                    super().save(update_fields=["foto_perfil"])

            except Exception as e:
                print(f"Error al procesar imagen WebP: {e}")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class HistorialPagos(models.Model):
    pass
