# Generated by Django 4.2.6 on 2023-11-15 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_bag_products_alter_bag_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bag',
            name='products',
        ),
        migrations.AddField(
            model_name='bag',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
