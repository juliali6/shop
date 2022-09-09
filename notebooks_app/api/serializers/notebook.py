from rest_framework import serializers

from category_app.api.serializers.category import BaseProductSerializer
from notebooks_app.models import Notebook


class NotebookSerializer(BaseProductSerializer, serializers.ModelSerializer):

    diagonal = serializers.CharField(required=True)
    display_type = serializers.CharField(required=True)
    processor_freq = serializers.CharField(required=True)
    ram = serializers.CharField(required=True)  # оперативная память
    video = serializers.CharField(required=True)
    time_without_charge = serializers.CharField(required=True)

    class Meta:
        model = Notebook
        fields = '__all__'