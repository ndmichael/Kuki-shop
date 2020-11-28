from django.urls import path
from shop import views as shop_views

app_name = 'shop'

urlpatterns = [
    path('', shop_views.index, name='shop-home'),
    path('category/', shop_views.product_list, name='product_list'),
    path('<slug:category_slug>/', shop_views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', shop_views.product_detail, name='product_detail'),   

]