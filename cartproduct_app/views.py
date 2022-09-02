from django.shortcuts import render
from django.views import View

from cartproduct_app.models import Cart
from category_app.models import Category
from customer_app.models import Customer


class CartView(View):

    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        cart = Cart.objects.get(owner=customer)
        categories = Category.objects.get_categories_for_left_sidebar()
        context = {
            'cart': cart,
            'categories': categories,
        }
        return render(request, 'cart.html', context)
