from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .signals import update_price

class Product(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=3,max_digits=19, default=0)
    manufacturer_company_name = models.CharField(max_length=100, blank=True)
    discount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    stock = models.PositiveBigIntegerField(default=0)
    is_available_after_stock= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"ID: {self.id}-UID: {self.uid}"

pre_save.connect(update_price, sender=Product)