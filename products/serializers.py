from rest_framework import serializers
from .models import Category, Product
from django.core.exceptions import ValidationError

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock_quantity', 'image_url', 'created_at', 'owner']
        read_only_fields = ['created_at', 'owner']

    def validate(self, data):
        product = Product(**data)

        try:
            product.clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        
        return data
    
    def create(self, validated_data):
        category_name = validated_data.pop('category').strip().lower()
        category, _ = Category.objects.get_or_create(name=category_name)