from django.db import models


class Bd(models.Model):
    title = models.CharField(
        max_length=50, null=True, verbose_name='Product'
    )
    content = models.TextField(
        null=True, blank=True, verbose_name='Description'
    )
    price = models.FloatField(
        null=True, blank=True, verbose_name='Price'
    )
    published = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Published'
    )

    class Meta:  # Служит для описания параметров самой модели
        verbose_name_plural = 'Advertisements'
        verbose_name = 'Advertisement'
        ordering = ['-published']  # сортировка по убыванию даты публикации
