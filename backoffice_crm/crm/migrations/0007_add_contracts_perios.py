# Generated by Django 5.1.1 on 2024-09-22 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_remove_contracts_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='contracts',
            name='period',
            field=models.DateField(null=False, blank=False)
        ),
    ]