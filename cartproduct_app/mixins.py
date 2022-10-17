from django.views import View

from cartproduct_app.models import Cart
from customer_app.models import Customer


class CartMixin(View):

    def dispatch(self, request, *args, **kwargs):
        """ Если пользователь авторизован - мы его ищем.
        Затем ищем корзину, которая относится к пользователю.
         Если она найдена мы ее возвращаем, если нет, то создаем новую корзину и возвращаем ее. """

        cart = None
        if request.user.is_authenticated:
            customer = Customer.objects.filter(user=request.user).first()
            if not customer:
                customer = Customer.objects.create(
                    user=request.user
                )
            cart = Cart.objects.filter(owner=customer, in_order=False).first()
            if not cart:
                cart = Cart.objects.create(owner=customer)
        self.cart = cart
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart
        return context


