from rest_framework import serializers

from customer_app.models import Customer, Order


class OrderSerializer(serializers.ModelSerializer):
    """Сериалайзер оформления заказов. """

    class Meta:
        model = Order
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    """Сериалайзер покупателей."""

    orders = OrderSerializer(many=True)

    class Meta:
        model = Customer
        fields = '__all__'
