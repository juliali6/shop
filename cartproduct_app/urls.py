from django.urls import path
from django.contrib.auth.decorators import login_required

from cartproduct_app.views.favourite import favourite_add, favourite_list
from cartproduct_app.views.cart import \
    CartView, \
    AddToCartView, \
    DeleteFromCartView, \
    ChangeQTYView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:ct_model>/<slug:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:ct_model>/<slug:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty-cart/<str:ct_model>/<slug:slug>/', ChangeQTYView.as_view(), name='change_qty'),
    path('fav/<int:id>/', login_required(favourite_add), name='favourite_add'),
    path('favourites', login_required(favourite_list), name='favourite_list'),
]
