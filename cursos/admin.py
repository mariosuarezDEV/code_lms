from django.contrib import admin

# Register your models here.
from .models import CategoriasModel, CursosModel


@admin.register(CategoriasModel)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion',
                    'fecha_creacion', 'usuario_modificacion', 'activo')
    list_editable = ('nombre', 'activo')
    search_fields = ('nombre',)

    readonly_fields = ("fecha_creacion", "fecha_modificacion",
                       "usuario_creacion", "usuario_modificacion")
    fieldsets = (
        (
            'Datos de la categoría',
            {
                'fields': ('nombre', 'descripcion', 'activo'),
                'classes': ('wide',)
            }
        ),
        (
            'Auditoría',
            {
                'fields': ('fecha_creacion', 'fecha_modificacion',
                           'usuario_creacion', 'usuario_modificacion'),
                'classes': ('collapse',)
            }
        )
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario_creacion = request.user
            obj.usuario_modificacion = request.user
        obj.usuario_modificacion = request.user
        return super().save_model(request, obj, form, change)


@admin.register(CursosModel)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'categoria',
                    'fecha_creacion', 'usuario_modificacion', 'activo')
    list_editable = ('nombre', 'categoria', 'activo')
    search_fields = ('nombre', 'descripcion')

    readonly_fields = ("fecha_creacion", "fecha_modificacion",
                       "usuario_creacion", "usuario_modificacion", 'num_estudiantes')
    fieldsets = (
        (
            'Datos del curso',
            {
                'fields': ('portada', 'nombre', 'descripcion', 'categoria', 'activo'),
                'classes': ('wide',)
            }
        ),
        (
            'Detalles del curso', {
                'fields': ('presentacion', 'nivel', 'precio'),
                'classes': ('wide',)
            }
        ),
        (
            'Auditoría',
            {
                'fields': ('fecha_creacion', 'fecha_modificacion',
                           'usuario_creacion', 'usuario_modificacion', 'num_estudiantes'),
                'classes': ('collapse',)
            }
        )
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario_creacion = request.user
            obj.usuario_modificacion = request.user
        obj.usuario_modificacion = request.user
        super().save_model(request, obj, form, change)
