from django.db import models

# Create your models here.

class Order(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()