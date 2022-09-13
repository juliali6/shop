from django.urls import path, include
from .api.views.router import api_router
from .views.checkout import CheckoutView
from .views.make_order import MakeOrderView

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    path('api/', include(api_router.urls)),

]
