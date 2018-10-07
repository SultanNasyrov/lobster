from django.urls import path, re_path
from .views import (cart, add_item, clean_cart, delete_item,
					change_quantity, order)


urlpatterns = [
    path('cart', cart, name='cart'),
    path('cart/add-item', add_item, name='add-item'),
    path('cart/clean', clean_cart, name='clean'),
    path('cart/delete-item', delete_item, name='delete-item'),
    path('cart/change-quantity', change_quantity, name="change-quantity"),
    path('cart/order', order, name='order')
    
]
