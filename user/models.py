from django.db import models


# Create your models here.


class User(models.Model):
    name = models.CharField(
        max_length=40, error_messages={"required": "This is the required field"}
    )
    email = models.EmailField()
    password = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    image = models.ImageField(upload_to="pics/")
