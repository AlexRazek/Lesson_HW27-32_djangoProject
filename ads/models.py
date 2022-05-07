from django.core.validators import MinLengthValidator
from django.db import models

from users.models import User



class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=10, validators=[MinLengthValidator(5)], unique=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Ad(models.Model):
    name = models.CharField(max_length=50, null=False, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(validators=[MinLengthValidator(0)])
    description = models.TextField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    is_published = models.CharField(max_length=20, default=True)
    image = models.ImageField(upload_to='logos/', null=True, blank=True)

    class Meta:
        verbose_name = "Обьявление"
        verbose_name_plural = "Обьявления"


class Selection(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)


    class Meta:
        verbose_name = "Подбор"
        verbose_name_plural = "Подборки"



    def __str__(self):
        return self.name