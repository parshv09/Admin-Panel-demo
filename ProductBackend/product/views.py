from django.shortcuts import render, redirect
from .models import Product,Category
from .forms import ProductForm
from django.shortcuts import get_object_or_404

def index_page(request):
    return render(request, 'products/index.html')

def pricing(request):
    return render(request, 'products/pricing-discounts.html')

def orders(request):
    return render(request, 'products/orders.html')

def customers(request):
    return render(request, 'products/customers.html')

def marketing(request):
    return render(request, 'products/marketing.html')

def omnichannel(request):
    return render(request, 'products/omnichannel.html')

def events(request):
    return render(request, 'products/events.html')

def reports(request):
    return render(request, 'products/reports.html')

def product_list(request):
    products = Product.objects.all()

    # Handle add product
    if request.method == 'POST' and not request.POST.get('product_id'):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product-list')

    # Handle edit product
    elif request.method == 'POST' and request.POST.get('product_id'):
        product = get_object_or_404(Product, pk=request.POST.get('product_id'))
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')

    else:
        form = ProductForm()
    categories = Category.objects.all()
    return render(request, 'products/products.html', {
        'products': products,
        'form': form,
        'categories':categories,
    })


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm(instance=product)

    products = Product.objects.all()
    return render(request, 'products/products.html', {
        'products': products,
        'form': form,
        'editing': True,
        'editing_product': product,
    })


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product-list')



# Display products to customers
def customer_view(request):
    products = Product.objects.all()
    return render(request, 'products/customer-view.html', {'products': products})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # ✅ Ensure cart is a dictionary, not list
    cart = request.session.get('cart')

    if not cart or not isinstance(cart, dict):
        cart = {}

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': float(product.price),  # Convert Decimal to float
            'image': product.image.url if product.image else '',
            'quantity': 1
        }

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('customer-view') 


def view_cart(request):
    cart = request.session.get('cart')
    if not cart or not isinstance(cart, dict):
        cart = {}

    total = sum(item['price'] * item['quantity'] for item in cart.values())

    return render(request, 'products/cart.html', {
        'cart': cart,
        'total': total
    })


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        del cart[product_id_str]
        request.session['cart'] = cart

    return redirect('view-cart')