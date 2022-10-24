from rest_framework import filters, permissions
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.reviews import ReviewSerializer
from ...models import Reviews


class ReviewViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    """Представление отзывов"""

    serializer_class = ReviewSerializer
    queryset = Reviews.objects.all()
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_field = ['id']
    permission_classes = [permissions.IsAuthenticated]
