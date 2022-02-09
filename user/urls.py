from django.contrib import admin
from django.urls import path
from . import views

# 空的為首頁，功能內部連結
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
