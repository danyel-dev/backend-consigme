# Generated by Django 4.2.6 on 2023-11-12 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_bag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bag',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='bag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.bag'),
        ),
    ]
