from django.db import models

# Create your models here.
class Customer(models.Model):
    name= models.CharField(max_length=200, null=True)
    phone= models.CharField(max_length=200, null=True)
    email= models.CharField(max_length=200, null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name= models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY=(
        ("Indoor","Indoor"),
        ("Outdoor","Outdoor")
        )
    name=models.CharField(max_length=200, null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200, null=True,choices=CATEGORY)
    description=models.CharField(max_length=200, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    tags=models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS=(
    ("Pending","Pending"),
    ("Out for delivery","Out for Delivery"),
    ("Delivered", "Delivered"),
    )
    date_created=models.DateTimeField(auto_now_add=True, null=False)
    customer=models.ForeignKey(Customer,null=False,on_delete=models.CASCADE)
    status=models.CharField(max_length=200,null=False,choices=STATUS)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=False)

    
