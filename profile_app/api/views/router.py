from rest_framework import routers
from .profile import ProfileView


api_router = routers.DefaultRouter()
api_router.register('profile', ProfileView)
