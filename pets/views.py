from rest_framework import generics
from .models import Category, PetType, PetStatus, Pet, Order, OrderStatus
from .serializers import CategorySerializer, PetTypeSerializer, PetStatusSerializer, PetSerializer, OrderSerializer, OrderStatusSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PetTypeListView(generics.ListAPIView):
    queryset = PetType.objects.all()
    serializer_class = PetTypeSerializer


class PetStatusListView(generics.ListAPIView):
    queryset = PetStatus.objects.all()
    serializer_class = PetStatusSerializer


class PetListView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
