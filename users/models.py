from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return self.name


class User(models.Model):
    ROLES = [
        ("member", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Администратор"),
    ]
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=25, null=True, blank=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=120)
    role = models.CharField(max_length=15, choices=ROLES, default="member")
    age = models.PositiveIntegerField()
    location_id = models.ManyToManyField(Location)
    image = models.ImageField(upload_to='media/')

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]



