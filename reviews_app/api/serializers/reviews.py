from rest_framework import serializers
from profile_app.api.serializers.profile import UserSerializer
from reviews_app.models import Reviews


class ReviewSerializer(serializers.ModelSerializer):
    """Сериалайзер отзывов"""

    class Meta:
        model = Reviews
        fields = '__all__'
        extra_kwargs = {
            'file': {
                'required': True,
                'write_only': True,
            },
        }

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )

    user = UserSerializer(read_only=True)