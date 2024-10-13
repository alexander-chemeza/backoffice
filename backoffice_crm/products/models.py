from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False, verbose_name='Наименование продукта')
    description = models.TextField(null=False, blank=False, verbose_name='Описание')
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Цена')

    def __str__(self):
        return self.name
