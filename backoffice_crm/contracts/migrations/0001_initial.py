# Generated by Django 5.1.1 on 2024-10-13 16:16

import django.db.models.deletion
import staff.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contracts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название контракта')),
                ('file', models.FileField(upload_to=staff.models.profile_file_path, verbose_name='Файл')),
                ('contract_date', models.DateField(verbose_name='Дата заключения контракта')),
                ('period', models.DateField(verbose_name='Дата окончания контракта')),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Полная стоимость')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='products.products', verbose_name='Услуга')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='customers.customers', verbose_name='Пользователь')),
            ],
        ),
    ]
