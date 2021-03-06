"""jcase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

# 空的為首頁，功能內部連結
urlpatterns = [
    path('', views.cases, name='cases'),
    path('create_case/', views.create_case, name='create_case'),
    path('case/<str:id>', views.case, name='case'),
    path('delete-case/<str:id>', views.delete_case, name='delete-case'),
    path('update-case/<str:id>', views.update_case, name='update-case'),
]
