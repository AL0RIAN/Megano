from django.db import models
from shop.models import Product
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Banner(models.Model):
    """
        Модель Banner представляет баннер для демонстрации пользователю продукта (модель Product),
        который можно приобрести по акции.
    """

    class Meta:
        ordering = ["updated_at"]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="banner")
    text = models.TextField(null=False, blank=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



