from django.contrib import admin
from .models import *

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['id', 'user', 'created_at', 'full_name', 'address']

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order, OrderAdmin)