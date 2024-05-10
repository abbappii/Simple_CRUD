from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model

from .signals import update_price

User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=3, max_digits=19, default=0)
    manufacturer_company_name = models.CharField(max_length=100, blank=True)
    discount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    stock = models.PositiveBigIntegerField(default=0)
    is_available_after_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    unit = models.CharField(max_length=100, blank=True)
    weight = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    packed_height = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    packed_weight = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    packed_length = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    user = models.ForeignKey(
        User, models.CASCADE, related_name="creator", null=True, blank=True
    )  # added null and blank to avoid migration non nullable

    def __str__(self) -> str:
        return f"ID: {self.id} - Title: {self.title}"


pre_save.connect(update_price, sender=Product)