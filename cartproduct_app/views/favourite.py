from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from category_app.models import Product


@login_required
def favourite_list(request):
    """Метод отображения избранных товаров"""

    product_fav = Product.objects.filter(favourites=request.user)
    return render(request, 'favourite.html', {'favourite_list': product_fav})


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

