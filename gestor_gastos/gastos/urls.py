from django.urls import path
from . import views

urlpatterns = [
    path('', views.resumen_quincenal, name='resumen'),
    path('duplicar-gastos/', views.duplicar_gastos, name='duplicar_gastos'),
]
