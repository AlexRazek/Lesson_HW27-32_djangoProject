from django.db import models


from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Ad(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    is_published = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    class Meta:
        verbose_name = "Обьявление"
        verbose_name_plural = "Обьявления"

    def __str__(self):
        return self.name