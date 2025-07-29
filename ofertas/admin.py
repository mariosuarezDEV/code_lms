from django.contrib import admin

# Register your models here.
from .models import OfertaModel


@admin.register(OfertaModel)
class OfertasAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descripcion', 'precio',
                    'fecha_creacion')
    search_fields = ('titulo', )
    readonly_fields = ('fecha_creacion', 'fecha_modificacion',
                       'usuario_creacion', 'usuario_modificacion', )

    fieldsets = (
        ('Información básica', {
            'fields': ('titulo', 'descripcion', 'precio')
        }),
        ('Actividad', {
            'fields': ('activo',)
        }),
        ('Auditoria', {
            'fields': ('fecha_creacion', 'fecha_modificacion', 'usuario_creacion', 'usuario_modificacion'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario_creacion = request.user
            obj.usuario_modificacion = request.user
        obj.usuario_modificacion = request.user
        return super().save_model(request, obj, form, change)
