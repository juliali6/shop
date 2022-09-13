from rest_framework import routers

from .registration import RegistrationViewSet
from .users import UserViewSet

api_router = routers.DefaultRouter()
api_router.register('users', UserViewSet)
api_router.register('registration', RegistrationViewSet)
