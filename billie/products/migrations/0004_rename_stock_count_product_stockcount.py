# Generated by Django 3.2.6 on 2021-08-31 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_stock_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stock_count',
            new_name='stockcount',
        ),
    ]
