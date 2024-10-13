from django.db import models
from products.models import Products
from customers.models import Customers
from staff.models import profile_file_path

class Contracts(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False, verbose_name='Название контракта')
    service = models.ForeignKey(Products, on_delete=models.CASCADE, null=False, blank=False, related_name='contracts', verbose_name='Услуга')
    file = models.FileField(upload_to=profile_file_path, null=False, blank=False, verbose_name='Файл')
    contract_date = models.DateField(null=False, blank=False, verbose_name='Дата заключения контракта')
    period = models.DateField(null=False, blank=False, verbose_name='Дата окончания контракта')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Полная стоимость')
    user = models.ForeignKey(Customers, on_delete=models.CASCADE, null=False, blank=False, related_name='customers', verbose_name='Пользователь')
