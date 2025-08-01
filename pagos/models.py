from django.db import models
from django.conf import settings
from base.models import BaseModel

# Create your models here.


class SponsorModelPago(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )  # Usuario que patrocina
