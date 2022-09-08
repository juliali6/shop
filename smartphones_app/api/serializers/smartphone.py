from rest_framework import serializers

from category_app.api.serializers.category import BaseProductSerializer
from smartphones_app.models import Smartphone


class SmartphoneSerializer(BaseProductSerializer, serializers.ModelSerializer):

    diagonal = serializers.CharField(required=True)
    display_type = serializers.CharField(required=True)
    resolution = serializers.CharField(required=True)  # разрешение экрана
    accum_volume = serializers.CharField(required=True)  # объем батареи
    ram = serializers.CharField(required=True)  # оперативная память
    sd = serializers.BooleanField(required=True)
    sd_volume_max = serializers.CharField(required=True)  # макс встр. памяти
    main_cam_mp = serializers.CharField(required=True)
    frontal_cam_mp = serializers.CharField(required=True)

    class Meta:
        model = Smartphone
        fields = '__all__'
