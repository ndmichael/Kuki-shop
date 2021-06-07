from django.shortcuts import render
from django.contrib.auth.models import User
from .models import OrderItem, Order
from .forms import OrderForm
from cart.cart import Cart
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from .tasks import order_created

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
import weasyprint


def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST, prefix='form1')
        print(request.POST)
        # print(c_form, end="\n")
        # print (form, end="\n")

        if form.is_valid():
            order = form.save(commit=False)
            order.user= request.user
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

            return render(request, 'orders/order/created.html', {'order': order})


    else:
        form = OrderForm (prefix='form1')
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})



@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename= "order_{}.pdf"'.format(order.id)
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])

    return response


def user_orders (request):
    user_id = request.user.id
    orders = Order.objects.filter(user=user_id)
    return orders