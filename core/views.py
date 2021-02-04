from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from .cart import Cart
from .models import Product
from .forms import CartAddForm
from django.views.decorators.http import require_POST


def products_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    return render(request, 'core/products_list.html', {'products': products, 'categories': categories, 'category': category, 'categories': categories})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    form = CartAddForm()
    return render(request, 'core/product_detail.html', {'product': product, 'form':form})


def detail(request):
	cart = Cart(request)
	return render(request, 'core/detail.html', {'cart':cart})

@require_POST
def cart_add(request, product_id):
    # session
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	form = CartAddForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(product=product, quantity=cd['quantity'])
	return redirect('core:detail')

# for removing cart item
def cart_remove(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.remove(product)
	return redirect('core:detail')