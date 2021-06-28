from django.db import models

# Create your models here.


class Product(models.Model):
    productName = models.CharField(max_length=70)
    productQuantity = models.DecimalField(max_digits=3, decimal_places=2)
    stock = models.DecimalField(max_digits=3, decimal_places=2)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(upload_to="pics/")
