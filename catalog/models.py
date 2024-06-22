from django.db import models

NULLBLE = {"blank": True, "null": True}


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="имя")
    description = models.TextField(verbose_name="описание")
    preview = models.ImageField(upload_to="products/", verbose_name="превью")
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        related_name="product",
        verbose_name="категория",
        **NULLBLE,
    )
    purchase_price = models.IntegerField(verbose_name="цена покупки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания ")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата последних изменений")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "purchase_price"]


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="имя")
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = [
            "name",
        ]