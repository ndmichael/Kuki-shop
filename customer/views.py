from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from orders.views import user_orders

# Create your views here.


@login_required
def dashboard(request):
    orders =  user_orders(request)
    context = {
        'orders': orders
    }
    return render(request, 'account/user/dashboard.html', context)