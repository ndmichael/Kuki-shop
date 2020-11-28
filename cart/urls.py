from django.urls import path
from . import views as cart_views



app_name = 'cart'

urlpatterns = [
    path('', cart_views.cart_detail, name='cart_detail'),
    path('addcart/', cart_views.cart_add_with_ajax, name='cart_add_with_ajax'),
    path('add/<int:product_id>/', cart_views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_views.cart_remove, name='cart_remove'),
]