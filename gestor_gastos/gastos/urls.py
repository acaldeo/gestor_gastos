from django.urls import path
from . import views
from .views import profile_view

urlpatterns = [
    path('', views.resumen_quincenal, name='resumen'),
    path('duplicar-gastos/', views.duplicar_gastos, name='duplicar_gastos'),
    path('crear-quincena/', views.crear_quincena, name='crear_quincena'),
    path('perfil/', profile_view, name='profile'),

]
