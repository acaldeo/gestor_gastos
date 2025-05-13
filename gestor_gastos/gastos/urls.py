# gastos/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GastoViewSet, IngresoViewSet, QuincenaViewSet

router = DefaultRouter()
#router.register(r'gastos', GastoViewSet)
router.register(r'ingresos', IngresoViewSet)
router.register(r'quincenas', QuincenaViewSet)
router.register(r'gastos', GastoViewSet, basename='gasto')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
]
