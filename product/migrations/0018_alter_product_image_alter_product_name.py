# Generated by Django 4.2.6 on 2023-12-06 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_alter_bag_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='media_root/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
