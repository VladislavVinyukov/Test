from rest_framework import serializers

from store.models import Product


class ProductAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'unit', 'price', 'updated_at']


class ProductViewSerializer(serializers.ModelSerializer):
    unit = serializers.CharField(source="get_unit_display")

    class Meta:
        model = Product
        fields = ['name', 'quantity', 'unit', 'price', 'updated_at']
