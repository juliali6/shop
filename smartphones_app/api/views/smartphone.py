from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from smartphones_app.api.serializers.smartphone import SmartphoneSerializer
from smartphones_app.models import Smartphone


class SmartphoneView(GenericViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):

    serializer_class = SmartphoneSerializer
    queryset = Smartphone.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']  # поиск








