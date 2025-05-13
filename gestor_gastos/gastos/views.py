# gastos/views.py

from rest_framework import viewsets, permissions
from .models import Gasto, Ingreso, Quincena
from .serializers import GastoSerializer, IngresoSerializer, QuincenaSerializer
from rest_framework.permissions import IsAuthenticated

class GastoViewSet(viewsets.ModelViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Gasto.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class IngresoViewSet(viewsets.ModelViewSet):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Ingreso.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)



class QuincenaViewSet(viewsets.ModelViewSet):
    queryset = Quincena.objects.all()
    serializer_class = QuincenaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Quincena.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
