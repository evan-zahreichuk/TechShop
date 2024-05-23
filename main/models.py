from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    brand = models.CharField(max_length=100, verbose_name='Бренд')
    name = models.CharField(max_length=200, verbose_name='Назва')
    specifications = models.TextField(verbose_name='Характеристики')
    description = models.TextField(verbose_name='Опис')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    img = models.CharField(max_length=350, verbose_name='Посилання на зображення')

    def __str__(self):
        return f"{self.brand} {self.name}"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    class Meta:
        verbose_name = 'Товар в кошику'
        verbose_name_plural = 'Товари в кошику'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    class Meta:
        verbose_name = 'Товар в замовленні'
        verbose_name_plural = 'Товари в замовленні'