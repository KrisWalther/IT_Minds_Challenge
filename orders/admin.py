from django.contrib import admin
from .models import Order, OrderItem

# Class for items in order
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

# Class for creating order based on email
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['email']
    inlines = [OrderItemInline]