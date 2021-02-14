from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model) :
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return f" {self.first_name} {self.last_name}"
        

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    # customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    # first_name = models.CharField(max_length=60)
    # last_name = models.CharField(max_length=60)
    # email = models.EmailField()
    address = models.CharField(max_length=250)
    design = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True) # this field is for transaction generated id
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.address)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                            related_name='order_items',
                            on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity