from django.views import View
from django.views.generic.detail import SingleObjectMixin

from category_app.models import Category, Product
from notebooks_app.models import Notebook
from smartphones_app.models import Smartphone


class CategoryDetailMixin(SingleObjectMixin):

    CATEGORY_SLUG2PRODUCT_MODEL = {
        'notebooks': Notebook,
        'smartphones': Smartphone,
    }

    def get_context_data(self, **kwargs):
        if isinstance(self.get_object(), Category):
            model = self.CATEGORY_SLUG2PRODUCT_MODEL[self.get_object().slug]
            context = super().get_context_data(**kwargs)
            context['categories'] = Category.objects.get_categories_for_left_sidebar()
            context['category_products'] = model.objects.all()
            return context
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.get_categories_for_left_sidebar()
        return context


class ProductMixin(View):
    """Миксин для вывода последних просмотренных товаров через Session"""

    def dispatch(self, request, *args, **kwargs):

        product_id = kwargs.get('id')

        recently_viewed_products = None

        if 'recently_viewed' in request.session:

            if product_id in request.session['recently_viewed']:
                request.session['recently_viewed'].remove(product_id)

            recently_viewed_products = Product.objects.filter(slug__in=request.session['recently_viewed'])
            request.session['recently_viewed'].insert(0, product_id)

            if len(request.session['recently_viewed']) > 5:
                request.session['recently_viewed'].pop()
        else:
            request.session['recently_viewed'] = [product_id]

        request.session.modified = True

        self.recently_viewed_products = recently_viewed_products

        return super().dispatch(request, *args, **kwargs)



