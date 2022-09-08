from rest_framework import routers

from category_app.api.views.category import CategoryView

api_router = routers.DefaultRouter()
api_router.register('categories', CategoryView)