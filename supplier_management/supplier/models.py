from django.db import models

from django.contrib.auth.models import User
from django.contrib.gis.db import models as gis_models


class Product(models.Model):
    supplier=models.ForeignKey(User,on_delete=models.CASCADE,related_name='products')
    name=modls.CharField(max_length=255)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    restock=models.PositiveIntegerField(default=10)
    location=gis_models.PointField(null=True,blank=True)


    def __str__(self):
        return self.name

    def needs_restocking(self):
        return self.stock <= self.restock_threshold

class Order(model.models):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    customer_name=models.CharField(max_length=200)
    shipping_address=models.TextField()
    location=gis_models.PointField(null=True,blank=True)
    status=models.CharField(
        max_length=50,
        choices=[
            ('pending', 'Pending'),
            ('shipped', 'Shipped'),
            ('delivered', 'Delivered'),
            ('cancelled', 'Cancelled'),
        ],
        default='pending',
    )


    def __str__(self):
        return f"order : {self.id}-{self.product.name}"


class Client(models.Model):
    sales_representative=models.ForeignKey(User,on_delete=models.CASCADE,related_name='clients')
    name=models.CharField(max_length=200)
    contact_details=models.TextField()
    location=gis_models.PointField(null=True,blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE, related_name='reviews')
    client=models.ForeignKey(Client,on_delete=models.Set_Null,null=True,blank=True)
    rating=models.PositiveIntegerField()
    comment=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Review for {self.product.name} by {self.client.name if self.client else 'Anonymous'}"
    

