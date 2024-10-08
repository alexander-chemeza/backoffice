# Generated by Django 5.1.1 on 2024-09-22 19:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_alter_services_cost_alter_services_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisements',
            name='budget',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Бюджет на рекламу'),
        ),
        migrations.AlterField(
            model_name='advertisements',
            name='channel',
            field=models.CharField(max_length=300, verbose_name='Название канала продвижения'),
        ),
        migrations.AlterField(
            model_name='advertisements',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Название рекламной кампании'),
        ),
        migrations.AlterField(
            model_name='advertisements',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='crm.services', verbose_name='Услуга'),
        ),
    ]
