from django.db import models

# Create your models here.

class FoodSales(models.Model):
    OrderDate = models.DateField(null=True, blank=True)
    Region = models.CharField(max_length=50, default='')
    City = models.CharField(max_length=50, default='')
    Category = models.CharField(max_length=50, default='')
    Product = models.CharField(max_length=50, default='')
    Quantity = models.IntegerField(default=" ")
    UnitPrice = models.DecimalField(max_digits=10,decimal_places=2,default='',null=True)

    def __str__(self):
        return self.City + self.Product
                 
    objects = models.Manager()
