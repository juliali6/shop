from django.db import models

from category_app.models import Product
from media_app.models import Media


class Reviews(models.Model):
    """Модель отзывов"""

    email = models.EmailField()
    name = models.CharField('Name', max_length=100)
    text = models.TextField('Message', max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name='Parent', on_delete=models.SET_NULL, blank=True, null=True
    )
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    file = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class MediaReview(models.Model):
    """Модель изображений в постах"""
    reviews = models.ForeignKey(Reviews, on_delete=models.CASCADE)
    image_reviews = models.ImageField(null=False, blank=True)
