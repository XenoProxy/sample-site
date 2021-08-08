from django.db import models


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Name')

    def __str__(self):  # Переопределение строкового представления класса
        return self.name

    class Meta:
        verbose_name_plural = 'Rubrics'
        verbose_name = 'Rubric'
        ordering = ['name']


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
    rubric = models.ForeignKey(
        'Rubric', null=True, on_delete=models.PROTECT, verbose_name='Rubric'
    )

    class Meta:  # Служит для описания параметров самой модели
        verbose_name_plural = 'Advertisements'
        verbose_name = 'Advertisement'
        ordering = ['-published']  # сортировка по убыванию даты публикации
