from django.contrib import admin
from .models import Category, Pet, PetType, PetStatus, Order, OrderStatus

admin.site.register(Category)
admin.site.register(Pet)
admin.site.register(PetType)
admin.site.register(PetStatus)
admin.site.register(Order)
admin.site.register(OrderStatus)