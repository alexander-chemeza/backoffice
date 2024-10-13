from django.db import models

class Leads(models.Model):
    last_name = models.CharField(max_length=200, blank=False, verbose_name='Фамилия')
    first_name = models.CharField(max_length=200, blank=False, verbose_name='Имя')
    surname = models.CharField(max_length=200, blank=False, verbose_name='Отчество')
    phone = models.CharField(max_length=200, blank=False, verbose_name='Телефон')
    email = models.EmailField(max_length=300, blank=False, verbose_name='Email')
    status = models.BooleanField(default=False, verbose_name='Статус')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.surname}'