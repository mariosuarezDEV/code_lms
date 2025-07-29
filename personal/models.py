from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    foto_perfil = models.ImageField(
        upload_to='perfil/', blank=True, null=True, verbose_name="Foto de perfil",
        help_text="Sube una foto de perfil")

    biografia = models.TextField(
        blank=True, null=True, verbose_name="Biografia", help_text="Escribe una biografía breve")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
