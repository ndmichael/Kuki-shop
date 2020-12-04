from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product
from cart.forms import CartAddForm
from cart.cart import Cart
from django.http import JsonResponse, HttpResponse

# Create your views here.


def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'shop/index.html', context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart_product_form = CartAddForm
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'products': products,
        'categories': categories,
        'title': 'textiles',
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/item_list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddForm
    categories = Category.objects.all()
    context = {
        'product': product,
        'title': product.category,
        'cart_product_form': cart_product_form,
        'categories': categories
    }
    return render(request, 'shop/product/item_detail.html', context)


