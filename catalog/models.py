from django.db import models

NULLBLE = {"blank": True, "null": True}


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="имя")
    description = models.TextField(verbose_name="описание")
    preview = models.ImageField(upload_to="products/", verbose_name="превью", **NULLBLE)
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


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="versions",
        verbose_name="продукт")
    version_number = models.CharField(max_length=10, verbose_name="версия")
    version_name = models.CharField(max_length=100, verbose_name="название версии")
    current_version = models.BooleanField(default=True, verbose_name="текущая версия")

    def __str__(self):
        return f"{self.product.name} - {self.version_number}"

    class Meta:
        verbose_name = "версия продукта"
        verbose_name_plural = "версии продуктов"