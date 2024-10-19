from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'quantity', 'ordered_at']
        read_only_fields = ['id', 'ordered_at']

        def create(self, validated_data):
            order = Order(**validated_data)
            order.save()
            
            return order