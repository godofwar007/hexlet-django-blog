from django.contrib import admin
from django.urls import path
from hexlet_django_blog import views

urlpatterns = [
    path('about/', views.about),
    path('', views.index),
    path('admin/', admin.site.urls),
]
