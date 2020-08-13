from django.shortcuts import render
from .models import OrderItem
from .forms import OrderForm
from cart.cart import Cart
from django.urls import reverse
from django.shortcuts import redirect, render
from .tasks import order_created

# Create your views here.


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            # Iterate over each items and create an orderItem for each item
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])


            # afterward successful order clear cart
            cart.clear()
            order_created.delay(order.id) 

            # set order in session
            request.session['order_id'] = order.id

            # redirect to payment
            return redirect(reverse('payment:process'))
            # return render(request, 'orders/order/created.html', {'order': order})

    else:
        form = OrderForm
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
