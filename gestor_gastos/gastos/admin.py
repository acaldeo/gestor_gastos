from django.contrib import admin
from .models import Gasto, Ingreso, Categoria, Quincena

class OwnerFilterAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return obj is None or obj.usuario == request.user

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return obj is None or obj.usuario == request.user

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return obj is None or obj.usuario == request.user

    def has_add_permission(self, request):
        return True

@admin.register(Gasto)
class GastoAdmin(OwnerFilterAdmin):
    pass

@admin.register(Ingreso)
class IngresoAdmin(OwnerFilterAdmin):
    pass

# Para Categoría y Quincena, podrías dejar acceso libre si son compartidas:
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Quincena)
class QuincenaAdmin(admin.ModelAdmin):
    pass

def save_model(self, request, obj, form, change):
    if not change or not obj.usuario:
        obj.usuario = request.user
    super().save_model(request, obj, form, change)
