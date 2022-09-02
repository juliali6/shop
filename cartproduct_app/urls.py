from django.urls import path

from cartproduct_app.views import CartView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
]