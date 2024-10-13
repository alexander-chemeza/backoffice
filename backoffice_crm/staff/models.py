from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def profile_file_path(instance: "Staff", filename: str) -> str:
    return "profiles/profile{pk}/files/{filename}".format(pk=instance.pk, filename=filename)


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('administrator', 'Администратор'), ('manager', 'Менеджер'), ('operator', 'Оператор'), ('marketer', 'Маркетолог')])

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Staff.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.staff.save()
