from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from core.models import Product
from .cart import Cart
from .forms import CartAddProductForm

# Post: Add item to cart
@require_POST # Requires submission
def cart_add(request, product_id):
    cart = Cart(request) # Cart of current request/session
    product = get_object_or_404(Product, id=product_id) # Get product by ID
    form = CartAddProductForm(request.POST) # Form to be processed
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                override_quantity=cd['override'])
    return redirect('cart:cart_detail') # Redirect to cart

# Post: Remove item from cart
@require_POST # Requires submission
def cart_remove(request, product_id):
    cart = Cart(request) # Cart of current request/session
    product = get_object_or_404(Product, id=product_id) # Get product by ID
    cart.remove(product)
    return redirect('cart:cart_detail') # Redirect to cart

# Update quantity of items in cart
def cart_detail(request):
    cart = Cart(request) # Cart of current request/session
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                'quantity': item['quantity'],
                'override': True})
    return render(request, 'cart/detail.html', {'cart': cart}) # Render cart details for each product based on template