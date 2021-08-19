from rest_framework.serializers import ModelSerializer

from store.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'unit', 'price', 'updated_at']
