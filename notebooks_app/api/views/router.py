from rest_framework import routers

from notebooks_app.api.views.notebook import NotebookView

api_router = routers.DefaultRouter()
api_router.register('notebooks', NotebookView)
