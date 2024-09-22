from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def profile_file_path(instance: "Profile", filename: str) -> str:
    return "profiles/profile{pk}/files/{filename}".format(pk=instance.pk, filename=filename)


class Services(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False, verbose_name='Наименование продукта')
    description = models.TextField(null=False, blank=False, verbose_name='Описание')
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Цена')

    def __str__(self):
        return self.name


class Advertisements(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False, verbose_name='Название рекламной кампании')
    channel = models.CharField(max_length=300, blank=False, null=False, verbose_name='Название канала продвижения')
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Бюджет на рекламу')
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=False, blank=False, related_name='advertisements', verbose_name='Услуга')

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=200, blank=False)
    first_name = models.CharField(max_length=200, blank=False)
    surname = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=300, blank=False)
    advertisement = models.ForeignKey(Advertisements, on_delete=models.CASCADE, null=True, blank=True, related_name='profile_advertisements')
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.surname}'


class Customer(models.Model):
    last_name = models.CharField(max_length=200, blank=False, verbose_name='Фамилия')
    first_name = models.CharField(max_length=200, blank=False, verbose_name='Имя')
    surname = models.CharField(max_length=200, blank=False, verbose_name='Отчество')
    phone = models.CharField(max_length=200, blank=False, verbose_name='Телефон')
    email = models.EmailField(max_length=300, blank=False, verbose_name='Email')
    advertisement = models.ForeignKey(Advertisements, on_delete=models.CASCADE, null=True, blank=True, related_name='customer_advertisements', verbose_name='Рекламная кампания')
    status = models.BooleanField(default=False, verbose_name='Статус')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.surname}'


class Contracts(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False, verbose_name='Название контракта')
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=False, blank=False, related_name='contracts', verbose_name='Услуга')
    file = models.FileField(upload_to=profile_file_path, null=False, blank=False, verbose_name='Файл')
    contract_date = models.DateField(null=False, blank=False, verbose_name='Дата заключения контракта')
    period = models.DateField(null=False, blank=False, verbose_name='Дата окончания контракта')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Полная стоимость')
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False, related_name='customers', verbose_name='Пользователь')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
