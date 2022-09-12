from django.contrib import messages
from django.db import transaction
from django.http import HttpResponseRedirect
from django.views import View

from cartproduct_app.mixins import CartMixin
from customer_app.forms.order import OrderForm
from customer_app.models import Customer


class MakeOrderView(CartMixin, View):
    """Класс оформления заказа."""

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        customer = Customer.objects.get(user=request.user)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.customer = customer
            new_order.first_name = form.cleaned_data['first_name']
            new_order.last_name = form.cleaned_data['last_name']
            new_order.phone = form.cleaned_data['phone']
            new_order.address = form.cleaned_data['address']
            new_order.buying_type = form.cleaned_data['buying_type']
            new_order.order_date = form.cleaned_data['order_date']
            new_order.comment = form.cleaned_data['comment']
            new_order.save()
            self.cart.in_order = True
            self.cart.save()
            new_order.cart = self.cart
            new_order.save()
            customer.orders.add(new_order)
            messages.add_message(request, messages.INFO, 'Thank you for your order! Expect a call')
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/checkout/')
