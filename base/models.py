from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class BaseModel(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='%(class)s_usuario_creacion')
    usuario_modificacion = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='%(class)s_usuario_modificacion')
    activo = models.BooleanField(default=True)

    class Meta:
        abstract = True
