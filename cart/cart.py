# from decimal import  Decimal
# from django.conf import settings
# from shop.models import Product
#
# class Cart(object):
#     def __init__(self, request):
#         '''
#             initialized cart here
#         '''
#         self.session = request.session
#         cart = self.session.get(settings.CART_SESSION_ID)
#
#         if not cart:
#             '''If no cart then save an empty cart in session'''
#             cart = self.session[settings.CART_SESSION_ID] = {}
#         self.cart = cart
#
#     def add(self, product, quantity=1, update_quantity=False):
#
#         product_id = str(product.id)
#         if product_id not in self.cart:
#             self.cart[product_id] = {'quantity': 0, 'price' : str(product.price)}
#         if update_quantity:
#             self.cart[product_id]['quantity'] = quantity
#         else:
#             self.cart[product_id]['quantity'] += quantity
#         self.save()
#
#     def save(self):
#         # This make sure the cart get saved
#         self.session.modified = True
#
#     def remove(self, product):
#         product_id = str(product.id)
#         if product_id in self.cart:
#             del self.cart[product_id]
#             self.save()
#
#     def __iter__(self):
#         product_ids = self.cart.keys()
#         products = Product.objects.filter(id__in = product_ids)
#         cart = self.cart.copy()
#         for product in products:
#             cart[str(product.id)]['product'] = product
#
#         for item in cart.values():
#             item['price'] = Decimal(item['price'])
#             item['total_price'] = item['price'] * item['quantity']
#             yield item
#
#     def __len__(self):
#         # counting item in cart by looping through the cart values
#         return sum(item['quantity'] for item in self.cart.values())
#
#     def get_total_price(self):
#         """
#         Getting total price you can decide to calculate and add discount here
#         i.e giving 5% discount, calling the len function discount for every 10 goods bought
#         """
#         return (item['price'] * item['quantity'] for item in self.cart.values())
#
#     def clear(self):
#         """
#         Clearing cart
#         """
#         del self.session[settings.CART_SESSION_ID]
#         self.save() # call the save method after clearing cart
#
#
#


from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
    """
        initializing cart
    """
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
            Add product to the cart or update it's quantity
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price': str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark session as modified to make sure it got saved.
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()












