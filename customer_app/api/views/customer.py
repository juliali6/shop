from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from customer_app.api.serializers.customer import CustomerSerializer
from customer_app.models import Customer


class CustomerView(GenericViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

