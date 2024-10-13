from django.db import models
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from ads.models import Ads
from leads.models import Leads


class Customers(models.Model):
    lead = models.ForeignKey(Leads, on_delete=models.CASCADE, null=False, blank=False, related_name='customer_leads', verbose_name='Потенциальный клиент')
    advertisement = models.ForeignKey(Ads, on_delete=models.CASCADE, null=False, blank=False, related_name='customer_advertisements', verbose_name='Рекламная кампания')

    def __str__(self):
        return f'{self.lead.first_name} {self.lead.last_name}'


@receiver(post_save, sender=Customers)
def update_lead_status_on_customer_save(sender, instance, created, **kwargs):
    instance.lead.status = True
    instance.lead.save()


@receiver(pre_save, sender=Customers)
def reset_old_lead_status_on_customer_update(sender, instance, **kwargs):
    if instance.pk:
        old_customer = Customers.objects.get(pk=instance.pk)
        if old_customer.lead != instance.lead:
            old_customer.lead.status = False
            old_customer.lead.save()


@receiver(pre_delete, sender=Customers)
def reset_lead_status_on_customer_delete(sender, instance, **kwargs):
    instance.lead.status = False
    instance.lead.save()

