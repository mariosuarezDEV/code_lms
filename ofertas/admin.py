from django.contrib import admin
from .models import OfertaCosteoModel


@admin.register(OfertaCosteoModel)
class OfertaCosteoAdmin(admin.ModelAdmin):
    list_display = ("id", "costo__titulo", "costo__precio", "fecha_creacion")
    search_fields = ("costo__titulo",)
    readonly_fields = (
        "fecha_creacion",
        "fecha_modificacion",
        "usuario_creacion",
        "usuario_modificacion",
    )
    fieldsets = (
        ("Información de la Oferta", {"fields": ("costo",)}),
        ("Actividad", {"fields": ("activo",)}),
        (
            "Auditoria",
            {
                "fields": (
                    "fecha_creacion",
                    "fecha_modificacion",
                    "usuario_creacion",
                    "usuario_modificacion",
                ),
                "classes": ("collapse",),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario_creacion = request.user
            obj.usuario_modificacion = request.user
        obj.usuario_modificacion = request.user
        return super().save_model(request, obj, form, change)
