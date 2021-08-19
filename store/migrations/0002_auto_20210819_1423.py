# Generated by Django 3.2.6 on 2021-08-19 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveBigIntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveBigIntegerField(default=0, verbose_name='Количество товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('p', 'Штук'), ('kg', 'Килограмм'), ('l', 'Литров')], default='p', max_length=20, verbose_name='Единица измерения'),
        ),
    ]
