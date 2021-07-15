from django.db import models


# Create your models here.


class User(models.Model):
    name = models.CharField(
        max_length=40, error_messages={"required": "This is the required field"}
    )
    email = models.EmailField(error_messages={"required": "This is the required field"})
    password = models.CharField(
        max_length=40, error_messages={"required": "This is the required field"}
    )
    address = models.CharField(
        max_length=40, error_messages={"required": "This is the required field"}
    )
    image = models.ImageField(
        upload_to="pics/", error_messages={"required": "This is the required field"}
    )
