from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

# Product list view
def product_list_view(request, category_slug=None):
    category = None
    categories = Category.objects.all() # View all categories
    products = Product.objects.all() # View all products
    if category_slug: # Filter products by category
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Render template
    return render(request, 'webshop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
        })

# Product detail view
def product_detail_view(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug) # Get product by ID and slug
    cart_product_form = CartAddProductForm() # Add to cart option

    # Render webshop template
    return render(request, 'webshop/product/detail.html', {
        'product': product,
        'cart_product_form': cart_product_form
        })