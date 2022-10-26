from django.contrib.contenttypes.models import ContentType
from django.views.generic import DetailView

from cartproduct_app.mixins import CartMixin
from category_app.mixins import CategoryDetailMixin
from notebooks_app.models import Notebook
from reviews_app.models import Reviews
from smartphones_app.models import Smartphone


class ProductDetailView(CartMixin, CategoryDetailMixin, DetailView):
    """Представление товаров."""

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
        content_type = ContentType.objects.get(model=self.model._meta.model_name).id
        context['reviews'] = Reviews.objects.filter(content_type=content_type)
        context['cart'] = self.cart
        return context
