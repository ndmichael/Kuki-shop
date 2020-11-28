from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import CartAddForm
from shop.models import Product
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponse


# Create your views here.

def cart_add_with_ajax(request):
    if request.POST.get('action') == 'post':        
        cart = Cart(request)
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(
            product= product,
        )
        cart_total = len(cart)
        return JsonResponse({"result": "Added Success", "cart_total": cart_total})
    return HttpResponse("Error access denied")


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product= product,
            quantity=cd['quantity'],
            update_quantity=cd['update']

        )
    return redirect('cart:cart_detail')





def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddForm(
            initial={'quantity': item['quantity'],
                     'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})






