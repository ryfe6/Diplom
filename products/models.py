from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    """Модель для создания объекта продукта."""

    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    price = models.PositiveIntegerField(
        verbose_name="Цена",
    )
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Продавец",
        on_delete=models.CASCADE,
        **NULLABLE,
    )
    is_sell = models.BooleanField(default=True, verbose_name="Признак продажи товара")

    def __str__(self):
        return f"Продавец {self.seller} продает продукт {self.name} за {self.price} рублей."

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
