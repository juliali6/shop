from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from cartproduct_app.mixins import CartMixin
from cartproduct_app.models import Cart, CartProduct
from category_app.models import Category
from customer_app.models import Customer


class AddToCartView(CartMixin, View):
    """Класс для добавления товаров в корзину.
    Проверка для добавления товара только один раз."""

    def get(self, request, *args, **kwargs):
        ct_model, product_slug = kwargs.get('ct_model'), kwargs.get('slug')
        content_type = ContentType.objects.get(model=ct_model)
        product = content_type.model_class().objects.get(slug=product_slug)
        cart_product, created = CartProduct.objects.get_or_create(
            user=self.cart.owner,
            cart=self.cart,
            content_type=content_type,
            object_id=product.id,
        )
        if created:
            self.cart.products.add(cart_product)
        return HttpResponseRedirect('/cart/')


class CartView(CartMixin, View):
    """Класс корзины пользователя"""

    def get(self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_left_sidebar()
        context = {
            'cart': self.cart,
            'categories': categories,
        }
        return render(request, 'cart.html', context)
