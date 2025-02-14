from django.contrib import admin
from django.urls import path, include
from hexlet_django_blog import views

urlpatterns = [
    path('about/', views.about),
    path('', views.index),
    path('articles/', include('hexlet_django_blog.article.urls')),

    path('admin/', admin.site.urls),

]
