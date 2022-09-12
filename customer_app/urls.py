from django.urls import path, include
from .api.views.router import api_router
from .views.authorization import AuthView
from .views.checkout import CheckoutView
from .views.logout import LogoutUser
from .views.make_order import MakeOrderView
from .views.registration import RegistrationView

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    path('api/', include(api_router.urls)),
    path('registration', RegistrationView.as_view(), name='reg_page'),
    path('login', AuthView.as_view(), name='login_page'),
    path('logout', LogoutUser.as_view(), name='logout_page'),

]
