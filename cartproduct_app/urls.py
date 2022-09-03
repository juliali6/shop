from django.urls import path

from cartproduct_app.views import CartView, AddToCartView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:ct_model>/<slug:slug>/', AddToCartView.as_view(), name='add_to_cart')
]