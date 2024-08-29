from django.shortcuts import render, get_object_or_404, redirect
from .models import Collection, Product, Cart
from decimal import Decimal

def home(request):
    collections = Collection.objects.all()

    partialCollections = []
    for collection in collections:
        partialProducts = collection.products.all()[:4]
        partialCollections.append({
            'collection': collection,
            'products': partialProducts
        })

    return render(request, 'home.html', {'partialCollections': partialCollections})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

def get_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return cart

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    quantity = int(request.POST.get('quantity', 1))

    if product_id_str in cart:
        cart[product_id_str]['quantity'] += quantity
    else:
        cart[product_id_str] = {
            'title': product.title,
            'price': str(product.price),
            'quantity': quantity,
            'image_url': product.image.url
        }

    request.session['cart'] = cart
    return redirect('cart_detail')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        cart[product_id_str]['quantity'] -= 1
        if cart[product_id_str]['quantity'] == 0:
            del cart[product_id_str]
        request.session['cart'] = cart

    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    total_price = Decimal('0.00')

    for product_id_str, item in cart.items():
        product = get_object_or_404(Product, id=int(product_id_str))
        item['discounted_price'] = product.discounted_price()
        item['total_price'] = item['discounted_price'] * item['quantity']
        total_price += item['total_price']

    return render(request, 'cart_detail.html', {'cart': cart, 'total_price': total_price})


def collection_view(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)
    products = Product.objects.filter(collection=collection)

    return render(request, 'collection_view.html', {
        'collection': collection,
        'products': products
    })

def sale_view(request):
    discounted_products = Product.objects.filter(discount__gt=0)

    return render(request, 'sale_view.html', {
        'products': discounted_products
    })
