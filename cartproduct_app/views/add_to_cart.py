from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.views import View

from cartproduct_app.mixins import CartMixin
from cartproduct_app.models import CartProduct
from cartproduct_app.utils import recalc_cart


class AddToCartView(LoginRequiredMixin, CartMixin, View):
    """Класс для добавления товаров в корзину.
    Проверка для добавления товара только один раз."""

    login_url = 'login'  # переадресация для неавторизованных пользователей

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
        recalc_cart(self.cart)
        messages.add_message(request, messages.INFO, "Product successfully added")
        return HttpResponseRedirect('/cart/')