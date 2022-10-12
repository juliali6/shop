from rest_framework.filters import SearchFilter
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from notebooks_app.api.serializers.notebook import NotebookSerializer
from notebooks_app.models import Notebook


class NotebookView(GenericViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    """Представление категории 'ноутбуков'."""

    serializer_class = NotebookSerializer
    queryset = Notebook.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']  # поиск
