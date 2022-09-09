from rest_framework import routers

from customer_app.api.views.customer import CustomerView

api_router = routers.DefaultRouter()
api_router.register('customers', CustomerView)