from django.db import models
from core.models import Product

# Class for creating orders based on email
class Order(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return f'Order {self.id}'
    
    # Total cost of order w/o discount
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

# Class for each item in the order
class OrderItem(models.Model):
    order = models.ForeignKey(Order,
            related_name='items',
            on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
            related_name='order_items',
            on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    # Cost of items w/o discount
    def get_cost(self):
        return self.price * self.quantity