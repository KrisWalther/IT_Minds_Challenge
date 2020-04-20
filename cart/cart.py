from django.conf import settings
from core.models import Product

# Cart class
class Cart(object):

    # Initialize cart: If session already exist: use old cart. Else: new cart
    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # Add product function
    def add(self, product, quantity=1, override_quantity=False):

        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    # Save if modified
    def save(self):
        
        self.session.modified = True

    # Remove product function
    def remove(self, product):

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # Function for iterating over products and associated prices in cart
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # Function for number of items in cart
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    # Function for returning discount
    def get_total_discount(self):
        if self.__len__() < 2: # If fewer than two items, then no discount
            return 0
        else: # Discount equal to number of items minus 1 times half the price
            return -int((self.__len__()-1)*100/2)

    # Function for returning the total price
    def get_total_price(self):
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values()) + self.get_total_discount()

    # Function for clearing cart
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()