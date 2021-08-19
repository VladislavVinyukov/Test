from django.db import models

PRODUCT_UNIT = [
    ('p', 'Штук'),
    ('kg', 'Килограмм'),
    ('l', 'Литров'),
]


# Create your models here.
class Product(models.Model):
    name = models.CharField("Название товара", max_length=255)
    quantity = models.PositiveBigIntegerField("Количество товара", default=0)
    unit = models.CharField("Единица измерения", max_length=20, choices=PRODUCT_UNIT, default="p",
                            help_text="p = Штук,kg = Килограмм,l = Литр")
    price = models.PositiveBigIntegerField("Цена", default=0)
    updated_at = models.DateTimeField("Дата последней поставки или отгрузки", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
