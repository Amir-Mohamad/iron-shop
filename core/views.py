from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def products_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    return render(request, 'core/products_list.html', {'products': products, 'categories': categories, 'category':category})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'core/product_detail.html', {'product': product})
