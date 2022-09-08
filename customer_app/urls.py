from django.urls import path

from customer_app.views import CheckoutView, MakeOrderView

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),

]