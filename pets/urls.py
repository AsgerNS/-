from django.urls import path
from .views import CategoryListView, PetTypeListView, PetStatusListView, PetListView, PetDetailView, OrderListView, OrderDetailView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('pet_types/', PetTypeListView.as_view(), name='pet_type_list'),
    path('pet_statuses/', PetStatusListView.as_view(), name='pet_status_list'),
    path('pets/', PetListView.as_view(), name='pet_list'),
    path('pets/<int:pk>/', PetDetailView.as_view(), name='pet_detail'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
]
