from user_app.api.serializers.users import UserSerializer
from profile_app.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    """Сериалайзер профиля пользователя"""

    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'avatar', 'phone', 'about',]
