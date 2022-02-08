from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=50, unique=True, null=False
    )
    createdom = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']  # id排序

    def __str__(self):
        return self.name  # 前端顯示用


class Amount(models.Model):
    name = models.CharField(
        max_length=50, unique=True, null=False
    )
    createdom = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']  # id排序

    def __str__(self):
        return self.name  # 前端顯示用


class Mode(models.Model):
    name = models.CharField(
        max_length=50, unique=True, null=False
    )
    createdom = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']  # id排序

    def __str__(self):
        return self.name  # 前端顯示用


class State(models.Model):
    name = models.CharField(
        max_length=50, unique=True, null=False
    )
    createdom = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']  # id排序

    def __str__(self):
        return self.name  # 前端顯示用


class Period(models.Model):
    name = models.CharField(
        max_length=50, unique=True, null=False
    )
    createdom = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']  # id排序

    def __str__(self):
        return self.name  # 前端顯示用
