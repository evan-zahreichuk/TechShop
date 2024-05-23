from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404

from main.forms import BrandFilterForm
from main.models import Product, CartItem, Order, OrderItem


def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')  # Перенаправлення неавторизованих користувачів на сторінку логіну

    query = request.GET.get('q')  # Отримання пошукового запиту
    form = BrandFilterForm(request.GET or None)

    if form.is_valid() and form.cleaned_data.get('brand'):
        products = Product.objects.filter(brand=form.cleaned_data['brand'])
    elif query:
        products = Product.objects.filter(name__icontains=query)  # Пошук за назвою товару
    else:
        products = Product.objects.all()

    return render(request, 'home.html', {'products': products, 'form': form})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1  # збільшуємо кількість, якщо товар вже в кошику
    cart_item.save()
    return redirect('home')


# views.py

def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')

        if full_name and address:
            order = Order.objects.create(user=request.user, full_name=full_name, address=address)
            for item in cart_items:
                OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
            cart_items.delete()  # Очищення кошика після оформлення замовлення
            return redirect('order_success')  # Перенаправлення на сторінку успішного оформлення замовлення
        # Тут можна додати повідомлення про помилку, якщо дані не введені

    return render(request, 'checkout.html', {'cart_items': cart_items})



def order_success(request):
    return render(request, 'order_success.html')



# views.py
def show_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    for item in cart_items:
        item.total_price = item.quantity * item.product.price
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price':total_price})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})


# В'юшка для реєстрації
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Перенаправлення на головну сторінку після реєстрації
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# В'юшка для авторизації
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Перенаправлення на головну сторінку після авторизації
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})  # Вірно вказаний шаблон авторизації


def logout_view(request):
    logout(request)
    return redirect('login')
