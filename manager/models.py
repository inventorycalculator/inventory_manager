from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User)
    productName = models.CharField(max_length = 30)
    buyCost = models.IntegerField(default = 0)
    sellCost = models.IntegerField(default = 0)
    salvageCost = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.productName

class Sale(models.Model):
    product = models.ForeignKey(Product)
    minSale = models.IntegerField(default = 0)
    probableSale = models.IntegerField(default = 0)
    maxSale = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.created_at
