from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class CartProduct(models.Model):

    user = models.ForeignKey('customer_app.Customer', verbose_name='Customer', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Cart', on_delete=models.CASCADE, related_name='cart')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total price')

    def __str__(self):
        return 'Product: {}'.format(self.product.title)


class Cart(models.Model):

    owner = models.ForeignKey('customer_app.Customer', verbose_name='Owner', on_delete=models.CASCADE)  # владелец
    products = models.ManyToManyField(CartProduct, blank=True, related_name='cart_product')
    total_product = models.PositiveIntegerField(default=0)  # отображение только уникальных продуктов
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total price')

    def __str__(self):
        return str(self.id)



