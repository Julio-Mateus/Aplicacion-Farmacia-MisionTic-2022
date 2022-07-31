from zarcosApp.models.orders import Orders
from rest_framework import serializers
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['date', 'totalsale']