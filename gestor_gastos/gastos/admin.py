from django.contrib import admin
from .models import Quincena, Categoria, Gasto, Ingreso

@admin.register(Quincena)
class QuincenaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin')
    ordering = ('fecha_inicio',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'monto', 'tipo', 'categoria', 'quincena', 'pagado')
    list_filter = ('tipo', 'categoria', 'quincena')
    search_fields = ('nombre',)

@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'monto', 'quincena')
    list_filter = ('quincena',)
    search_fields = ('descripcion',)
