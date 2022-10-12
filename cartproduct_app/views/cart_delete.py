from django.http import HttpResponseRedirect
from django.views import View
from django.contrib import messages
from cartproduct_app.mixins import CartMixin
from django.contrib.contenttypes.models import ContentType

from cartproduct_app.models import CartProduct
from cartproduct_app.utils import recalc_cart


class DeleteFromCartView(CartMixin, View):
    """Класс удаления товаров из корзины."""

    def get(self, request, *args, **kwargs):
        ct_model, product_slug = kwargs.get('ct_model'), kwargs.get('slug')
        content_type = ContentType.objects.get(model=ct_model)
        product = content_type.model_class().objects.get(slug=product_slug)
        cart_product= CartProduct.objects.get(
            user=self.cart.owner,
            cart=self.cart,
            content_type=content_type,
            object_id=product.id,
        )
        self.cart.products.remove(cart_product)
        cart_product.delete()
        recalc_cart(self.cart)
        messages.add_message(request, messages.INFO, "Product successfully deleted")
        return HttpResponseRedirect('/cart/')