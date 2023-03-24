
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.HelloView.as_view(), name ='hello'),
]