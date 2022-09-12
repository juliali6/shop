from django.shortcuts import render
from django.views import View

from cartproduct_app.mixins import CartMixin
from category_app.models import Category
from customer_app.forms.order import OrderForm


class CheckoutView(CartMixin, View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_left_sidebar()
        form = OrderForm(request.POST or None)
        context = {
            'cart': self.cart,
            'categories': categories,
            'form': form,
        }
        return render(request, 'checkout.html', context)
