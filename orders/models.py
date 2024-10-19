from django.db import models
from products.models import Product
from users.models import User
from django.core.exceptions import ValidationError

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.quantity <= 0:
            raise ValidationError('Quantity cannot be zero it must be greater than zero.')
        
        if self.product.stock_quantity < self.quantity:
            raise ValidationError(f'Insufficient stock for {self.product} try a lower amount please.')
        
    def save(self, *args, **kwargs):
        self.full_clean()
        self.product.stock_quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)

    def get_order_status(self):
        if self.product.stock_quantity < self.quantity:
            return (f'Insufficient stock, stock left is{self.product.stock_quantity}.')
        
        return ('In stock')

# Create your models here.
