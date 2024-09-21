from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def profile_file_path(instance: "Profile", filename: str) -> str:
    return "profiles/profile{pk}/files/{filename}".format(pk=instance.pk, filename=filename)


class Services(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)
    description = models.TextField(null=False, blank=False)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)


class Advertisements(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)
    channel = models.CharField(max_length=300, blank=False, null=False)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=False, blank=False, related_name='advertisements')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=200, blank=False)
    first_name = models.CharField(max_length=200, blank=False)
    surname = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=300, blank=False)
    advertisement = models.ForeignKey(Advertisements, on_delete=models.CASCADE, null=True, blank=True, related_name='advertisements')
    status = models.BooleanField(default=False)


class Contracts(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=False, blank=False, related_name='contracts')
    file = models.FileField(upload_to=profile_file_path, null=False, blank=False)
    contact_date = models.DateField(null=False, blank=False)
    period = models.IntegerField(null=False, blank=False)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='users')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
