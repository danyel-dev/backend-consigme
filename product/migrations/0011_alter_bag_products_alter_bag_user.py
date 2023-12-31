# Generated by Django 4.2.6 on 2023-11-15 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0010_alter_bag_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bag',
            name='products',
            field=models.ManyToManyField(blank=True, to='product.product'),
        ),
        migrations.AlterField(
            model_name='bag',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
