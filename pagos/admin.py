from django.contrib import admin

# Register your models here.
from .models import HistorialPagos


@admin.register(HistorialPagos)
class HistorialPagosAdmin(admin.ModelAdmin):
    list_display = ["usuario", "folio", "monto", "fecha", "descripcion"]
