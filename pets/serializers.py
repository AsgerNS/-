from rest_framework import serializers
from .models import Pet, Category, PetStatus, Order, OrderStatus, PetType


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetStatus
        fields = '__all__'


class PetSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    status = PetStatusSerializer()

    class Meta:
        model = Pet
        fields = '__all__'


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    pet = PetSerializer()
    status = OrderStatusSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class PetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetType
        fields = '__all__'
