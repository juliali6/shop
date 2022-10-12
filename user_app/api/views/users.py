from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from user_app.api.serializers.users import UserSerializer
from ...models import User


class UserViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    """Представление регистрации юзера"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
