from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class CartProduct(models.Model):
    """Модель корзины.
    Характеристики."""

    user = models.ForeignKey('customer_app.Customer', verbose_name='Customer', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Cart', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total price')

    def __str__(self):
        return 'Product: {}'.format(self.content_object.title)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.content_object.price
        super().save(*args, **kwargs)


class Cart(models.Model):
    """Модель оформения товара через корзину."""

    owner = models.ForeignKey('customer_app.Customer', null=True, verbose_name='Owner', on_delete=models.CASCADE)  # владелец
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_product = models.PositiveIntegerField(default=0)  # отображение только уникальных продуктов
    final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Total price')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


