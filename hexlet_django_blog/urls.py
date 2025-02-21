from django.contrib import admin
from django.urls import path, include
from hexlet_django_blog.views import HomePage, about


urlpatterns = [
    path('about/', about),
    path('', HomePage.as_view()),
    path('articles/', include('hexlet_django_blog.article.urls')),

    path('admin/', admin.site.urls),

]
