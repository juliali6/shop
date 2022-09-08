from rest_framework import routers

from smartphones_app.api.views.smartphone import SmartphoneView

api_router = routers.DefaultRouter()
api_router.register('smartphones', SmartphoneView)
