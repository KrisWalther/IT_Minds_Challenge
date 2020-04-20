from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

# Function for creating order
def order_create(request):
    cart = Cart(request) # Cart based on request/session
    if request.method == 'POST': # If submitted, process form
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart: # Create an order item for each item in cart
                OrderItem.objects.create(order=order,
                        product=item['product'],
                        price=item['price'],
                        quantity=item['quantity'])

            cart.clear() # Clear cart

            # Render order confirmation template
            return render(request,
                    'orders/order/created.html',
                    {'order': order})
    else: # If not submitted, display empty form
        form = OrderCreateForm()
    
    # Render order creation template
    return render(request,
            'orders/order/create.html',
            {'cart': cart, 'form': form})