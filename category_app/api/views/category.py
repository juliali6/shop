from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from category_app.api.serializers.category import CategorySerializer
from category_app.models import Category


class CategoryView(GenericViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    """Представление категорий товаров."""

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
