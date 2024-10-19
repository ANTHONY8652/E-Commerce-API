from django.contrib import admin
from .models import Order
from django.utils.translation import gettext_lazy as _

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity', 'stock_status', 'ordered_at', 'get_order_status']
    list_filter = ['ordered_at', 'user', 'product']
    search_fields = ['user__username', 'product__name', 'ordered_at']
    ordering = ['ordered_at']

    def get_order_status(self, obj):
        return obj.get_order_status()
    
    get_order_status.short_description = _('Order Status')

    def stock_status(self, obj):
        return 'In_Stock' if obj.product.stock_quantity >= obj.quantity else 'Insuficcient Stock' 
    stock_status.short_description = _('Stock Status')

    def mark_as_fulfilled(self, request, queryset):
        for order in queryset:
            if order.product.stock_quantity >= order.quantity:
                order.product.stock_quantity -= order.quantity
                order.product.save()
                order.save()
            
            else:
                self.message_user(request, f'Order {order.id} has insufficient stock.', level='error')
            
        self.message_user(request, 'Selected orders have been fulfilled.', level='success')
        
    mark_as_fulfilled.short_description = ('Mark selected orders as fulfilled.')

    actions = [mark_as_fulfilled]


admin.site.register(Order, OrderAdmin)



# Register your models here.
