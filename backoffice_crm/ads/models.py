from django.db import models
from products.models import Products

class Ads(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False, verbose_name='Название рекламной кампании')
    channel = models.CharField(max_length=300, blank=False, null=False, verbose_name='Название канала продвижения')
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Бюджет на рекламу')
    service = models.ForeignKey(Products, on_delete=models.CASCADE, null=False, blank=False, related_name='advertisements', verbose_name='Услуга')

    def __str__(self):
        return self.name