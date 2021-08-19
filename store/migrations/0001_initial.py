# Generated by Django 3.2.6 on 2021-08-19 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название товара')),
                ('quantity', models.PositiveBigIntegerField(verbose_name='Количество товара')),
                ('unit', models.CharField(choices=[('p', 'Штук'), ('kg', 'Килограмм'), ('l', 'Литров')], max_length=20, verbose_name='Единица измерения')),
                ('price', models.PositiveBigIntegerField(verbose_name='Цена')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата последней поставки или отгрузки')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
