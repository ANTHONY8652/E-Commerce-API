from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'created_at', 'user']

        def validate_ratinf(self, value):
            if not (1 <= value <= 5):
                raise serializers.ValidationError('Rating must be between 1 and 5.')
            
            return value
        
        def create(self, validated_data):
            user = validated_data.pop('user')
            review = Review.objects.create(user=user, **validated_data)

            return review
        
        def update(self, instance, validated_data):
            instance.rating = validated_data.get('rating', instance.rating)
            instance.comment = validated_data.get('comment', instance.comment)
            instance.save()
            return instance