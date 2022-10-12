from django.shortcuts import render
from django.views import View

from cartproduct_app.mixins import CartMixin
from category_app.models import Category, LatestProducts


class BaseView(CartMixin, View):
    """Основной класс представления"""

    def get(self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_left_sidebar()
        products = LatestProducts.objects.get_products_for_main_page(
            'notebook', 'smartphone', with_respect_to='smartphones'
        )
        context = {
            'categories': categories,
            'products': products,
            'cart': self.cart,
        }
        return render(request, 'base.html', context)
