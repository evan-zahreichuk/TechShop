from django.urls import path
from .views import *

urlpatterns = [
    path('register', register, name='register'),  # URL для реєстрації
    path('login', login_view, name='login'),      # URL для авторизації
    path('', home, name='home'),
    path('add-to-cart/<int:product_id>', add_to_cart, name='add_to_cart'),
    path('cart', show_cart, name='show_cart'),
    path('checkout', checkout, name='checkout'),
    path('order-success', order_success, name='order_success'),
    path('product/<int:product_id>', product_detail, name='product_detail'),
    path('logout', logout_view, name='logout'),  # URL для виходу користувача
]
