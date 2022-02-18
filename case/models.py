from django.db import models
from user.models import Profile, Respondent
from django.db.models.deletion import SET_NULL, CASCADE
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


class Case(models.Model):
    owner = models.ForeignKey(Profile, on_delete=CASCADE)  # 不需填寫
    title = models.CharField(max_length=200)
    view = models.IntegerField(default=0)  # 不需填寫
    contact = models.CharField(max_length=100)

    description = models.TextField(null=True, blank=True)
    skill = models.TextField(null=True, blank=True)
    createdon = models.DateTimeField(auto_now_add=True)  # 不需填寫

    category = models.ForeignKey(Category, null=True, on_delete=SET_NULL)
    amount = models.ForeignKey(Amount, null=True, on_delete=SET_NULL)
    period = models.ForeignKey(Period, null=True, on_delete=SET_NULL)
    state = models.ForeignKey(
        State, null=True, on_delete=SET_NULL, default='新進案')

    respondent = models.ManyToManyField(Respondent)
    mode = models.ManyToManyField(Mode)

    class Meta:
        ordering = ['-createdon']

    def __str__(self):
        return f'{self.id}-{self.title}'
