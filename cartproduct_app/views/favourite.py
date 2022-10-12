from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View

from cartproduct_app.mixins import CartMixin
from category_app.models import Product, Category


class FavouriteList(CartMixin, View):
    """Представление избранных товаров"""

    def get(self, request):

        product_fav = Product.objects.filter(favourites=request.user)
        categories = Category.objects.get_categories_for_left_sidebar()
        context = {
            'favourite_list': product_fav,
            'categories': categories,
            'cart': self.cart
        }
        return render(request, 'favourite.html', context)


@login_required
def favourite_add(request, id):
    """Метод добавления избранных товаров"""

    product = get_object_or_404(Product, id=id)
    if product.favourites.filter(id=request.user.id).exists():
        product.favourites.remove(request.user)
        messages.add_message(request, messages.INFO, 'Removed from your favorites')
    else:
        product.favourites.add(request.user)
        messages.add_message(request, messages.INFO, 'Added to favorites')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

