from django.urls import path

from category_app.views import test_view, ProductDetailView

urlpatterns = [
    path('', test_view, name='base'),
    path('products/<str:ct_model>/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),

]
