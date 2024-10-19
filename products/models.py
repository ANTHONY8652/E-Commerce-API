from django.db import models
from users.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock_quantity = models.PositiveBigIntegerField(validators=[MinValueValidator(0)])
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def clean(self):
        if not self.name:
            raise ValidationError('Name is required.')
        
        if self.price <= 0:
            raise ValidationError('Price must be greater than zero.')
        
        def __str__(self):
            return f'{self.name} is {self.price}'

# Create your models here.
