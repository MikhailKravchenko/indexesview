from rest_framework import serializers

from .models import Price


class PriceListSerializer(serializers.ModelSerializer):
    # price_id = serializers.ModelSerializer.serializer_field_mapping
    market = serializers.CharField(max_length=100),
    name_coin = serializers.CharField(max_length=100),
    price = serializers.FloatField()
    update_at = serializers.DateTimeField

    class Meta:
        model = Price
        fields = (['market', 'name_coin', 'price', 'update_at'])
