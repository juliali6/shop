from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from media_app.api.serializers.media import MediaSerializer
from ...models import Media


class MediaViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin):
    """Представление медиа."""

    serializer_class = MediaSerializer
    queryset = Media.objects.all()
