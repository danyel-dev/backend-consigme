# Generated by Django 4.2.6 on 2023-11-14 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_bag_product_product_bag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bag',
        ),
        migrations.AddField(
            model_name='bag',
            name='products',
            field=models.ManyToManyField(to='product.product'),
        ),
    ]
