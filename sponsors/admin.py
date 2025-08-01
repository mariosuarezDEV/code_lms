from django.contrib import admin

# Register your models here.
from .models import SponsorCosteoModel


@admin.register(SponsorCosteoModel)
class SponsorCosteoAdmin(admin.ModelAdmin):
    list_display = ("id", "costo__titulo", "costo__precio")
    search_fields = ("costo__titulo",)
    readonly_fields = (
        "fecha_creacion",
        "fecha_modificacion",
        "usuario_creacion",
        "usuario_modificacion",
    )
    list_filter = ("activo",)
    ordering = ("-fecha_creacion",)
    list_per_page = 20
    list_display_links = ("id", "costo__titulo")
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
