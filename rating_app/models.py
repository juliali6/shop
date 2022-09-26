from django.db import models

from category_app.models import Product


class RatingStar(models.Model):
    """Модель звезд рейтинга"""

    value = models.SmallIntegerField('Value', default=0)

    def __str__(self):
        return f'{self.value}'


class Meta:
    verbose_name = "Rating star"
    verbose_name_plural = "Rating star"
    ordering = ["-value"]


class Rating(models.Model):
    """Модель рейтинга"""

    ip = models.CharField('IP address', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='star')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product')

    def __str__(self):
        return f"{self.star} - {self.product}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Rating"




