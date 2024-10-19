from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'created_at']
    search_fields = ['product__name', 'user__username']
    list_filter = ['rating', 'created_at']
    ordering = ['created_at']
    raw_id_fields = ['product', 'user']
    date_hierarchy = 'created_at'

admin.site.register(Review, ReviewAdmin)


# Register your models here.
