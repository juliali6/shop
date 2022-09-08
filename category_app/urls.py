from category_app.views import BaseView, ProductDetailView, CategoryDetailView

from django.urls import path, include
from .api.views.router import api_router

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('products/<str:ct_model>/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('api/', include(api_router.urls)),

]
