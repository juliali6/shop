from rest_framework import serializers

from media_app.models import Media


class MediaSerializer(serializers.ModelSerializer):
    """Сериазайзер медиа."""

    class Meta:
        model = Media
        fields = '__all__'
        read_only_fields = ['user']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user',
    )
