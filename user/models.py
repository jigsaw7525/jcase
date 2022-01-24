from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import SET_NULL
from sympy import Point
# Create your models here.


class City(models.Model):
    name = models.CharField(
        max_length=50, unique=True, null=False
    )
    createdom = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']  # id排序

    def __str__(self):
        return f'{self.name}'


class Respondent(models.Model):
    name = models.CharField(
        max_length=50, unique=True, null=False
    )
    createdom = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']  # id排序

    def __str__(self):
        return f'{self.id}-{self.name}-{self.createdom}'


class Profile(AbstractUser):
    point = models.ImageField(default=0)
    certification = models.BooleanField(default=False)
    city = models.ForeignKey(City, on_delete=SET_NULL, null=True)
    respondent = models.ForeignKey(Respondent, on_delete=SET_NULL, null=True)

    def __str__(self):
        return f'{self.username}'
