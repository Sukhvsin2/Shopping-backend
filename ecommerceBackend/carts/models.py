from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # if order is not checked out then false otherwise true
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return self.user.username + " " + str(self.total_price)


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user.username + '\'s cart') + " " + str(self.product.product_name)

# This calls exactly after the cartItem is added
@receiver(pre_save, sender=CartItems)
def my_handler(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_product = Product.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(price_of_product.product_price)

    # updating count particular product like milk - 2
    # total_cart_item = CartItems.objects.filter(user=cart_items.user)

    # All cart Item Update
    # cart = Cart.objects.get(id=cart_items.cart.id)
    # cart.total_price += cart_items.price
    # cart.save()

