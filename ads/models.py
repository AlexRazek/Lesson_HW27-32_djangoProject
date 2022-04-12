from django.db import models
from uuid import uuid4


class Category(models.Model):
    name = models.CharField(max_length=30)

class Ad(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, null=True)
    address = models.CharField(max_length=250)
    is_published = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.name