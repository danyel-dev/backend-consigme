# Generated by Django 4.2.7 on 2023-12-11 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_profile_house_number_alter_profile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cep',
            field=models.CharField(default='06565436398', max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(default='Santo Inácio', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='complement',
            field=models.CharField(default='Ao lado do frigorifico', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='district',
            field=models.CharField(default='Centro', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='house_number',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(default='PI', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='street',
            field=models.CharField(default='Avenida Getúlio Vargas', max_length=50),
            preserve_default=False,
        ),
    ]
