from rest_framework import serializers
from .models import Asset
from .utils import get_live_price

class AssetSerializer(serializers.ModelSerializer):
    current_value = serializers.SerializerMethodField()

    class Meta:
        model = Asset
        fields = ['id', 'symbol', 'quantity', 'purchase_price', 'current_value']

    def get_current_value(self, obj):
        # This integrates the 3rd party API into our Read operation
        live_price = get_live_price(obj.symbol.lower())
        return live_price * obj.quantity