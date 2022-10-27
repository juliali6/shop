from django.urls import path, include

from .api.views.router import api_router
from .views.base import BaseView
from .views.category_detail import CategoryDetailView
# from .views.product import product
from .views.product_detail import ProductDetailView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('products/<str:ct_model>/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    # path('product/<int:product_id>/', product, name='product'),
    path('api/', include(api_router.urls)),

]
