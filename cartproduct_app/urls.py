from django.urls import path
from django.contrib.auth.decorators import login_required

from cartproduct_app.views.add_to_cart import AddToCartView
from cartproduct_app.views.cart_delete import DeleteFromCartView
from cartproduct_app.views.favourite import favourite_add, FavouriteList
from cartproduct_app.views.cart import CartView
from cartproduct_app.views.qty_cart import ChangeQTYView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:ct_model>/<slug:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:ct_model>/<slug:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty-cart/<str:ct_model>/<slug:slug>/', ChangeQTYView.as_view(), name='change_qty'),
    path('fav/<int:id>/', favourite_add, name='favourite_add'),
    path('favourites', FavouriteList.as_view(), name='favourite_list'),
]
