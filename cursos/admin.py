from django.contrib import admin

# Register your models here.
from .models import CategoriasModel, CursosModel, AlumnosInscritosModel


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


class AlumnosInscritosInline(admin.TabularInline):
    model = AlumnosInscritosModel
    extra = 1
    autocomplete_fields = ('alumno',)
    verbose_name = "Alumnos inscritos"
    verbose_name_plural = "Alumnos inscritos"

    readonly_fields = ("fecha_creacion", "fecha_modificacion",
                       "usuario_creacion", "usuario_modificacion")

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario_creacion = request.user
            obj.usuario_modificacion = request.user
        obj.usuario_modificacion = request.user
        super().save_model(request, obj, form, change)


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

    inlines = [AlumnosInscritosInline]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario_creacion = request.user
            obj.usuario_modificacion = request.user
        obj.usuario_modificacion = request.user
        super().save_model(request, obj, form, change)


@admin.register(AlumnosInscritosModel)
class AlumnosInscritosAdmin(admin.ModelAdmin):
    list_display = ['alumno', 'curso', 'fecha_inscripcion']
    list_filter = ['curso__categoria', 'curso__nivel']
    search_fields = ['alumno__username', 'alumno__email', 'curso__nombre']

    readonly_fields = ("fecha_creacion", "fecha_modificacion",
                       "usuario_creacion", "usuario_modificacion", 'fecha_inscripcion')

    fieldsets = (
        (
            'Datos de inscripción',
            {
                'fields': ('alumno', 'curso', 'fecha_inscripcion',
                           'activo'),
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
        super().save_model(request, obj, form, change)
