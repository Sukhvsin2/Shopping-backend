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
        return self.user.username


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    total_items = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)


@receiver(post_save, sender=CartItems)
def my_handler(sender, **kwargs):
    print('This is post Save')
