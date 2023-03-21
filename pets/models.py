from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class PetType(models.Model):
    name = models.CharField(max_length=255)


class PetStatus(models.Model):
    name = models.CharField(max_length=255)


class Pet(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='pets')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pet_type = models.ForeignKey(PetType, on_delete=models.CASCADE)
    status = models.ForeignKey(PetStatus, on_delete=models.CASCADE)


class OrderStatus(models.Model):
    name = models.CharField(max_length=255)


class Order(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
