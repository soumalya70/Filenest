from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('home/', home),
    path('login/', login,name='login'),
    path('register/', register,name='register'),
    path('logout/', logout, name='logout'),
    path('fileview/<id>/', fileview, name='fileview'),
    path('fileview/', fileview, name='fileview'),
]
