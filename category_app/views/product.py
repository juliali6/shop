from django.shortcuts import render
from django.views.generic import DetailView

from cartproduct_app.mixins import CartMixin
from category_app.mixins import CategoryDetailMixin
from category_app.models import Product
from notebooks_app.models import Notebook
from rating_app.forms.rating import RatingForm
from smartphones_app.models import Smartphone


class ProductDetailView(CartMixin, CategoryDetailMixin, DetailView):

    CT_MODEL_MODEL_CLASS = {
        'notebook': Notebook,
        'smartphone': Smartphone,
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    # model = Model
    # queryset = Model.objects.all()
    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ct_model'] = self.model._meta.model_name
        context['cart'] = self.cart
        context['star_form'] = RatingForm
        return context


def product(request, product_id):
    """Метод представления последних просмотренных товаров.
    Макс. к-л 5 товаров."""

    product = Product.objects.get(pk=product_id)
    recently_viewed_products = None

    if 'recently_viewed' in request.session:
        if product_id in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(product_id)

        products = Product.objects.filter(pk__in=request.session['recently_viewed'])
        recently_viewed_products = sorted(products,
                                          key=lambda x:request.session['recently_viewed'].index(x.id))
        request.session['recently_viewed'].insert(0, product_id)
        if len(request.session['recently_viewed']) > 5:
            request.session['recently_viewed'].pop()
    else:
        request.session['recently_viewed'] = [product_id]

    request.session.modified = True

    context = {'product': product, 'c': recently_viewed_products}
    return render(request, 'product_detail.html', context)
