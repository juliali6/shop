from rest_framework import routers

from reviews_app.api.views.reviews import ReviewViewSet

api_router = routers.DefaultRouter()
api_router.register('review', ReviewViewSet)
