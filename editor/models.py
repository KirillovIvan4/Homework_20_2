from django.db import models
NULLBLE = {"blank": True, "null": True}


class Publications(models.Model):
    title = models.CharField(max_length=100, verbose_name="имя")
    slug = models.CharField(max_length=150, verbose_name="slug", **NULLBLE)
    body = models.TextField(verbose_name="содержимое")
    preview = models.ImageField(upload_to="article/", verbose_name="превью")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания ")
    is_published = models.BooleanField(default=True, verbose_name="опубликовано")
    views_count = models.IntegerField(default=0, verbose_name="просмотры")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'