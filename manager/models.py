from django.db import models

# Create your models here.
# User
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User)
    productName = models.CharField(max_length = 50)
    buyCost = models.IntegerField(default = 0)
    sellCost = models.IntegerField(default = 0)
    salvageCost = models.IntegerField(default = 0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.productName

class Sale(models.Model):
    product = models.ForeignKey(Product)
    minSale = models.IntegerField(default = 0)
    probableSale = models.IntegerField(default = 0)
    maxSale = models.IntegerField(default = 0)
    date = models.DateTimeField('date created')

    def __str__(self):
        return self.date
