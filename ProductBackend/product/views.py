from django.shortcuts import render, redirect
from .models import Product,Category
from .forms import ProductForm
from django.shortcuts import get_object_or_404

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
