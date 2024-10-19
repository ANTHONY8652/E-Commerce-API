from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category','stock_quantity', 'owner', 'created_at']
    list_filter = ['category', 'owner']
    search_fields = ['name', 'category', 'price', 'created_at']
    date_hierarchy = 'created_at'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


# Register your models here.
