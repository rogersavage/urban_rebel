from django.db import models
from decimal import Decimal, ROUND_HALF_UP

class Collection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    collection = models.ForeignKey(Collection, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def discounted_price(self):
        discount_factor = Decimal(self.discount) / Decimal(100)
        discounted_price = self.price * (1 - discount_factor)
        return discounted_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

class Cart(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart ({self.user.username})"

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_total_price(self):
        return self.product.price * self.quantity
