# gastos/serializers.py

from rest_framework import serializers
from .models import Gasto, Ingreso, Quincena

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = ['id', 'monto', 'descripcion', 'fecha', 'categoria']  # usuario excluido

    def create(self, validated_data):
        # Asociamos automáticamente el usuario al crear el gasto
        validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)

class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields = '__all__'
        read_only_fields = ['usuario']

    def create(self, validated_data):
        validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)


class QuincenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quincena
        fields = '__all__'
        read_only_fields = ['usuario']

    def create(self, validated_data):
        validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)
