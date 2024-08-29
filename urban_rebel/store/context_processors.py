from .models import Collection

def cart_item_count(request):
    cart = request.session.get('cart', {})
    count = sum(item['quantity'] for item in cart.values())
    return {'cart_item_count': count}

def collections_processor(request):
    collections = Collection.objects.all()
    return {'collections': collections}
