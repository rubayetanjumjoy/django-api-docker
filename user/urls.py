
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('userlist/', views.UserList.as_view(), name ='user'),
]