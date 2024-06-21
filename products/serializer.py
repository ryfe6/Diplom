from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Сериалайзер для работы с пользователем."""

    class Meta:
        model = Product
        fields = ["name", "description", "price"]

    def to_representation(self, instance):
        if instance.is_sell:
            representation = super().to_representation(instance)
            representation["price"] = round(
                instance.price / 0.78,
            )
            return representation


class ProductSerializerSeller(serializers.ModelSerializer):
    """Сериалайзер для работы с продавцом."""

    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "seller", "is_sell"]
