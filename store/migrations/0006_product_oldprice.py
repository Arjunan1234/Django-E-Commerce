# Generated by Django 5.0.1 on 2024-02-02 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='oldprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
