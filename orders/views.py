from django.shortcuts import render
from django.contrib.auth.models import User
from .models import OrderItem, Order, Customer
from .forms import OrderForm, CustomerForm
from cart.cart import Cart
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from .tasks import order_created

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
import weasyprint

# Create your views here.

def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        c_form = CustomerForm(request.POST, prefix='form1') 
        # test = c_form.save()  
         
        form = OrderForm(request.POST, prefix='form2') 
        print(request.POST)  
        # print(c_form, end="\n")
        # print (form, end="\n")

        if form.is_valid() :
            if request.user.is_authenticated:     
                order = form.save(commit=False)
                customer = Customer.objects.create(user=request.user, first_name= request.user.first_name , 
                            last_name= request.user.last_name , email= request.user.email)
                order.customer = customer
                order = form.save()
            
            else:
                if form.is_valid() and c_form.is_valid():
                    anony = c_form.save()
                    order = form.save(commit=False)
                    customer = Customer.objects.create(user=None, first_name= anony.first_name , 
                            last_name= anony.last_name , email= anony.email)
                    print(customer)
                    order.customer = customer
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
        form = OrderForm (prefix='form2')
        c_form = CustomerForm (prefix='form1')
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form, 'c_form': c_form})



@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename= "order_{}.pdf"'.format(order.id)
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])

    return response

