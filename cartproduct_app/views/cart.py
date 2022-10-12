from django.shortcuts import render
from django.views import View

from cartproduct_app.mixins import CartMixin
from category_app.models import Category


class CartView(CartMixin, View):
    """Представление корзины пользователя"""

    def get(self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_left_sidebar()
        context = {
            'cart': self.cart,
            'categories': categories,
        }
        return render(request, 'cart.html', context)
